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
    _send_stack = []
    _receive_stack = ["Hello World!"]
    
    #Client's constructor
    def __init__(self, ip, port, state = False):
        self._server_ip = ip
        self._server_port = port
        self._is_blocking = state

    #A simple wrapper function that connects to a sever
    def start_connection(self):
        try:
            print("Connecting...")
            self._client_socket.connect((self._server_ip, self._server_port))
        except:
            print("Could not connect.")
        else:
            self._is_connected = True
            print("Connected")

    #A simple wrapper function to put outbound data on the send stack
    #Data is appended(pushed) on to the rear of the stack
    def send(self, data):
        self._send_stack.append(data)

    #A simple wrapper function to put inbound data on the receive stack
    #Data is read from index 0 and then popped off the front of the stack
    def receive(self):
        try:
            data = self._receive_stack[0]
            self._receive_stack.pop(0)
            return data
        except:
            print("No data on receive stack.")
    
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
        if blocking:
            self._is_blocking = True
            self._client_socket.setblocking(True)
        else:
            self._is_blocking = False
            
    
if __name__ == '__main__':
    #Creation of the client object
    client = Client("127.0.0.1", 8990, False)

    #Starts the socket connection
    client.start_connection()

    '''
    #An example of popping receive data from the receive stack
    print(client._receive_stack)
    print(client.receive())
    print(client._receive_stack)
    '''

    '''
    #An example of pushing send data to the send stack
    print(client._send_stack)
    client.send("Hello World!")
    print(client._send_stack)
    ''' 

    #Used to gracefully close the connction
    client.close_connection()
        
