import socket as s
import sys

def validate_ip_address(ip_address):
    try:
        s.inet_aton(ip_address)
        return True
    except s.error:
        return False

def start_server(ip_address, port, user):
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    try:
        server_socket.bind((ip_address, port))
        server_socket.listen(1)
        print("Connected.")

        client_socket, client_address = server_socket.accept()
        print(f"Connection established at {client_address}")

        while True:
            received_message = client_socket.recv(1024).decode()
            if not received_message or received_message.lower() == "end":
                print("Connection closed by client.")
                break

            print(f"{user}: {received_message}")

            response_message = input("Enter your message: ")
            client_socket.send(response_message.encode())

            if response_message.lower() == "end":
                print("End")
                break

    except s.error as e:
        print(f"Socket error: {e}")

    finally:
        client_socket.close()
        server_socket.close()

def get_ip_address():
    ip_address = input("Enter the IP address (or press Enter for localhost): ")
    if ip_address == "":
        ip_address = "localhost"
    elif not validate_ip_address(ip_address):
        print("Invalid IP address format. Please enter a valid IP address.")
        sys.exit(1)
    return ip_address

def get_port():
    port = input("Enter port number (or press Enter for default port): ")
    if port == "":
        port = 8080
    else:
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number. Please enter a valid port number.")
            sys.exit(1)
    return port

def get_username():
    return input("Enter your username: ")

def main():
    try:
        ip_address = get_ip_address()
        port = get_port()
        user = get_username()
        start_server(ip_address, port, user)
    except KeyboardInterrupt:
        print("\nServer terminated by user.")
        sys.exit()

if __name__ == "__main__":
    main()