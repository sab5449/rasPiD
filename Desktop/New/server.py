import socket

class Server:
    def __init__(self):
        self.TCP_IP = socket.gethostbyname(socket.gethostname())
        print self.TCP_IP
        self.PORT = 5005
        self.BUFFER_SIZE = 1024

    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.TCP_IP, self.PORT))
        s.listen(1)

        conn, addr = s.accept()
        print 'Connection address:', addr

        while 1:
            data = conn.recv(self.BUFFER_SIZE)
            if not data: break
            print "received data:", data
            conn.send(data)
        conn.close()

 

                    
                    
