import socket
import threading

class Client():

    # Server data
    _server_ip = ""
    _server_port = 0

    # Client's socket
    _client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Client's State Data
    _is_connected = False
    _is_blocking = False

    # Client's Data Stacks
    _send_stack = []
    _receive_stack = []

    # Clients send/receive threads
    _tx_thread = None
    _rx_thread = None
    
    # Client's constructor
    def __init__(self, ip, port, state = False):
        self._server_ip = ip
        self._server_port = port
        self._is_blocking = state

    # A simple wrapper function that connects to a sever
    def start_connection(self):
        try:
            print("Connecting...")
            self._client_socket.connect((self._server_ip, self._server_port))
        except:
            print("Could not connect.")
        else:
            self._is_connected = True
            
            # This is the transmit thread
            self._tx_thread = threading.Thread(target=self._send)
            self._tx_thread.start()

            # This is the receive thread
            self._rx_thread = threading.Thread(target=self._recv)
            self._rx_thread.start()
            
            print("Connected")
    
    #---------------------DO NOT CALL THESE FUNCTIONS!--------------------------
    # Instead use the respective functions receive and send to interact through
    # their respective data stacks, as these functions are ment to be threaded at
    # start-up of the socket object
    
    # This is a back-end function for putting data on to the receive stack
    def _recv(self):
        while True:
            if self._is_connected == False:
                break
            try:
                data = self._client_socket.recv(1024)
                self._receive_stack.append(repr(data))
                #print("Receiving...")
            except:
                #print("Cound not/nothing to receive.")
                pass
            

    # This is a back-end function to send data from the send stack
    def _send(self):
        while True:
            if self._is_connected == False:
                break
            try:
                self._client_socket.sendall(self._send_stack[0])
                self._send_stack.pop(0)
                #print("Sending...")
            except:
                #print("Could not/nothing to send.")
                pass
            
    #---------------------------------------------------------------------------
    

    # A simple wrapper function to put outbound data on the send stack
    # Data is appended(pushed) on to the rear of the stack
    def send(self, data):
        self._send_stack.append(data)

    # A simple wrapper function to put inbound data on the receive stack
    # Data is read from index 0 and then popped off the front of the stack
    def receive(self):
        try:
            data = self._receive_stack[0]
            self._receive_stack.pop(0)
            return data
        except:
            #print("No data on receive stack.")
            pass
    
    # A simple wrapper function that gracefully closes the connection
    def close_connection(self):
        self._client_socket.close()
        self._is_connected = False
        
    # Getters
    def get_server_ip(self):
        return self._server_ip

    def get_server_port(self):
        return self._server_port

    def get_connection_status(self):
        return self._is_connected

    def get_blocking_state(self):
        return self._is_blocking

    # Setters
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
    # Creation of the client object
    client = Client("127.0.0.1", 8990, False)

    # Starts the socket connection
    client.start_connection()

    while True:
    #-------An example of sending data through the higher level interface-------
    # The process behind this is:
    # 1. Higher level function pushes data onto the send stack
    # 2. A thread running the low level _send function sends the data
    # 3. The low level function then pops the send stack
    # There should be normally no data left on the send stack as demonstrated:

        client.send(b"Hello World!")
        #client._send() # Should not be normally called, should be in a thread
        #print("stack after send:", client._send_stack)

    #---------------------------------------------------------------------------

    
    #------An example of receiving data through the higher level interface------
    # The process behind this is:
    # 1. A thread running the low level function pushes data onto the receive
    #    stack
    # 2. The high level receive function is called to retrieve data from stack
    # 3. The high level function then pops the receive stack
    # There can be data left one the receive stack if high level function is not
    # used to retrieve. The data will just be queued up.

    #client._recv() # Should not be normally called, should be in a thread
        client.receive()
        #print(client.receive())
        #print("stack after receive:", client._receive_stack)

    #---------------------------------------------------------------------------


    '''
    # An example of popping receive data from the receive stack
    print(client._receive_stack)
    print(client.receive())
    print(client._receive_stack)
    '''

    '''
    # An example of pushing send data to the send stack
    print(client._send_stack)
    client.send("Hello World!")
    print(client._send_stack)
    '''

    # Used to gracefully close the connction
    client.close_connection()
        
