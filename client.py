import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def send_message():
    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))


def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(f"\n{message.decode('utf-8')}")
        except:
            print("Error receiving message.")
            client_socket.close()
            break

send_thread = threading.Thread(target=send_message)
send_thread.start()

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()
