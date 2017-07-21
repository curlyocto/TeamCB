import socket

class Client():

    #Server data
    server_ip = ""
    server_port = 0

    #Client's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Client's State Data
    is_connected = False

    #Client's constructor
    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = port

    #A simple wrapper function that connects to a sever
    def start_connect(self):
        try:
            print("Connecting...")
            self.client_socket.connect((self.server_ip, self.server_port))
        except:
            print("Could not connect.")
        else:
            self.is_connected = True
            print("Connected")
            
    #A simple wrapper function that gracefully closes the connection
    def close_connection(self):
        self.client_socket.close()
        self.is_connected = False
        
    #Getters
    def get_server_ip(self):
        return self.server_ip

    def get_server_port(self):
        return self.server_port

    def get_connection_status(self):
        return self.is_connected

    #Setters
    def set_server_ip(self, ip):
        self.server_ip = ip

    def set_server_port(self, port):
        self.server_port = port

    def set_connection_status(self, status):
        self.is_connected
    
if __name__ == '__main__':
    client = Client("127.0.0.1", 8990)
    client.start_connect()
    client.close_connection()

    while(client.get_connection_status()):
        print("Connected")

    quit()

