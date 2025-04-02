# Add your solution here
import socket
import threading
import sys

SERVER_IP = '0.0.0.0'
CLIENT_BUFFER = 2048
lock = threading.Lock()  # Для потокобезопасной работы со списком
mean_data = 0
calls_number = 0


def handle_client(conn, addr):
    global mean_data, calls_number
    try:
        print(f"Server: got connection to {addr}")
        number = int(conn.recv(CLIENT_BUFFER).decode())
        with lock:
            general = mean_data * calls_number + number
            calls_number += 1
            mean_data = general / calls_number
        print(
            f"Server: received {number} from {addr}, new mean_data {mean_data}")
        print(f"Server waits ready message from {addr}")

        flag = conn.recv(CLIENT_BUFFER).decode()
        if flag == "ready":
            print(
                f"Server: got ready message from {addr}, sending {mean_data}")
            conn.send(str(mean_data).encode())

    finally:
        conn.close()


def main():
    port = int(sys.argv[1])
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, port))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen()
    print(f"Server: listening on {SERVER_IP}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
    except KeyboardInterrupt:
        print("Server: stopped")
        server_socket.close()


if __name__ == "__main__":
    main()
