import socket as s
import sys

def validate_ip_address(ip_address):
    try:
        s.inet_aton(ip_address)
        return True
    except s.error:
        return False

def connect_to_server(host_ip, port):
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    try:
        client_socket.connect((host_ip, port))
        print("Connected to the server.")
        return client_socket
    except s.error as e:
        print(f"Failed to connect to server: {e}")
        sys.exit()

def start_client(client_socket):
    try:
        while True:
            message = input("Enter your message: ")
            client_socket.send(message.encode())

            if message.lower() == "end":
                print("Ending conversation...")
                break

            received_message = client_socket.recv(1024).decode()
            if not received_message:
                print("Connection closed by server.")
                break

            print("Server:", received_message)

            if received_message.lower() == "end":
                print("Ending conversation.")
                break

    except Exception as e:
        print("An error occurred:", e)

    finally:
        client_socket.close()

def get_host_ip():
    host_ip = input("Enter the server's IP address: ")
    if not validate_ip_address(host_ip):
        print("Invalid IP address. Please provide a valid IP address.")
        sys.exit(1)
    return host_ip

def get_port():
    port = input("Enter the server's port number: ")
    if not port:
        print("Please provide a valid port number.")
        sys.exit(1)
    try:
        port = int(port)
        return port
    except ValueError:
        print("Invalid port number. Port must be an integer.")
        sys.exit(1)

def main():
    try:
        host_ip = get_host_ip()
        port = get_port()
        client_socket = connect_to_server(host_ip, port)
        start_client(client_socket)
    except KeyboardInterrupt:
        print("\nClient terminated by user.")
        sys.exit()

if __name__ == "__main__":
    main()