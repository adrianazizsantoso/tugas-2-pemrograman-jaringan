import socket
import threading
import logging
import time

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(32).decode('utf-8')
            if data:
                response = self.process_request(data)
                self.connection.sendall(response.encode('utf-8'))
                if data.endswith("QUIT\r\n"):
                    break
            else:
                break
        self.connection.close()

    def process_request(self, request):
        if request.startswith("TIME") and request.endswith("\r\n"):
            current_time = time.strftime("%H:%M:%S", time.localtime())
            response = f"JAM {current_time}\r\n"
        else:
            response = "Invalid request\r\n"
        return response

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 55000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")
            print(f"Connection from {self.client_address}")
            
            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()
