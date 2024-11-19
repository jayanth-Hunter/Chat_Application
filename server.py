import socket
import threading

SERVER_HOST = '127.0.0.1' 
SERVER_PORT = 12345 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)  
clients = [] 

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Message received: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                clients.remove(client_socket)
                break
        except:
            clients.remove(client_socket)
            break
def accept_clients():
    print("Server is listening for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection: {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

accept_clients_thread = threading.Thread(target=accept_clients)
accept_clients_thread.start()
