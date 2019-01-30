# Simple port connection/listen script with two usages:
#  simport -l host port (Listen)
#  simport host port (Connection)

import select
import socket
import sys

def listen(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, int(port)))
    s.listen()

    (client_sock, client_addr) = s.accept()

    io_loop(client_sock)

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, int(port)))

    io_loop(s)

def io_loop(socket):
    input = [socket, sys.stdin]
    running = True

    while running:
        # Select waits for input (or output), or multiple streams and when any has input, it returns a list of ready streams
        input_ready, output_ready, except_ready = select.select(input, [], [])

        for input_stream in input_ready:
            if input_stream == socket:
                print(str(socket.recv(1024), 'utf-8'))

            elif input_stream == sys.stdin:
                user_typed = sys.stdin.readline()
                user_typed == user_typed[:-1]
                if user_typed == 'exit':
                    running = False
                else:
                    socket.send(bytes(user_typed, 'utf-8'))

if sys.argv[1] == "-l":
    listen(sys.argv[2], sys.argv[3])
else:
    connect(sys.argv[1], sys.argv[3])