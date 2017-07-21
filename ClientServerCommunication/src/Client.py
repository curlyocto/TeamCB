import socket

class Client():

    #Server data
    _server_ip = ""
    _server_port = 0

    #Client's socket
    _client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Client's State Data
    _is_connected = False
    _is_blocking = False

    #Client's Data Stacks
    _to_send = []
    _to_receive = []
    
    #Client's constructor
    def __init__(self, ip, port):
        self._server_ip = ip
        self._server_port = port

    #A simple wrapper function that connects to a sever
    def start_connect(self):
        try:
            print("Connecting...")
            self._client_socket.connect((self.server_ip, self.server_port))
        except:
            print("Could not connect.")
        else:
            self._is_connected = True
            print("Connected")

    #A simple wrapper function to put outbound data on the send stack
    def send(self, data):
        #TODO: Implement
        pass

    #A simple wrapper function to put inbound data on the receive stack
    def receive(self):
        #TODO: Implement
        pass
    
    #A simple wrapper function that gracefully closes the connection
    def close_connection(self):
        self._client_socket.close()
        self._is_connected = False
        
    #Getters
    def get_server_ip(self):
        return self._server_ip

    def get_server_port(self):
        return self._server_port

    def get_connection_status(self):
        return self._is_connected

    def get_blocking_state(self):
        return self._is_blocking

    #Setters
    def set_server_ip(self, ip):
        self._server_ip = ip

    def set_server_port(self, port):
        self._server_port = port

    def set_connection_status(self, status):
        self._is_connected

    def set_blocking_state(self, blocking):
        self._is_blocking = blocking
    
if __name__ == '__main__':
    client = Client("100.112.57.238", 8990)
    client.start_connect()
    client.close_connection()

    while(client.get_connection_status()):
        print("Connected")


        
