import socket
import sys

# send a request through code rather than brower
def http_get_request(server_host, server_port, filename):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect the socket to the server
        client_socket.connect((server_host, server_port))
        
        # Send HTTP GET request
        request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
        client_socket.sendall(request.encode())
        
        # Receive response from the server
        # `response = b""` initializes an empty byte string to store the server's response.
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data
        
        # Decode and display the server's response
        print(response.decode('utf-8'))
    
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py server_host server_port filename")
        sys.exit(1)
    
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    
    http_get_request(server_host, server_port, filename)

# usage: client.py server_host server_port filename