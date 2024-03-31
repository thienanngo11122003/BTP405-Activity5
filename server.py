# server.py
import socket
import threading

def handle_client(client_socket, client_num):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print(f"Received from client {client_num}")
            if message.lower() == 'quit':
                print(f"Closing connection with client {client_num}...")
                break
            client_socket.sendall(data)
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    print(f"Waiting for connections...\n")

    client_num = 0
    while True:
        client_socket, client_address = server_socket.accept()
        client_num += 1
        print(f"Accepted connection from client {client_num}: {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_num))
        client_thread.start()
    
    server_socket.close()


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 65432
    start_server(HOST, PORT)

