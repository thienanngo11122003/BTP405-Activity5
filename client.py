# client.py
import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        message = input("Enter message to send (type 'quit' to exit): ").strip()
        client_socket.sendall(message.encode())
        if message.lower() == 'quit':
            break
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode()}")

    print("Closing connection...")
    client_socket.close()

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 65432
    start_client(HOST, PORT)
