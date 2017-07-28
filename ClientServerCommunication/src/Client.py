# David Hansen
# Updated 7/27/17
# A client socket script with basic functionality

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
        # Closes connection gracefully
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
            
    
if __name__ == "__main__":
    # Creation of the client object
    client = Client("127.0.0.1", 8990, False)

    # Starts the socket connection
    client.start_connection()

    # The send/receive loop
    while True:
        
        # recv is placed first so that you see your response after you type
        # TODO: make this solution less hacky
        print(client.receive())

        # Stores input
        s = input()

        # Encodes the string and sends it
        client.send(s.encode("utf-8"))

        # A way to quit
        if s == "/quit":
            break
  
    # Used to gracefully close the connction
    client.close_connection()
        
