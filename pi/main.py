import SocketServer
from tracker import *

class RequestHandler(SocketServer.BaseRequestHandler):

    targetTracker = Tracker()

    #Request is a number coresponding to the signiture we want to retrieve data for    
    def handle(self):
        while (True):
            print("Print request reived, Handling")
            self.data = self.request.recv(1024)
            print(self.data)
            print(type(self.data))
            print(len(self.data))
            self.data = self.data.strip()
            print(self.data)
            print(type(self.data))
            print(len(self.data))
            self.data = self.data
            print(self.data)
            if self.data == 1:#Find the vision target CCC
                print("Going to track signature from 1st if")
                self.request.sendall(self.targetTracker.trackSignature(0))
                print("wrote data to wfile")
            elif self.data == 2:#Potentially tracking color wheel Video
                print("Going to track color from 2nd if")
                self.request.sendall(self.targetTracker.trackColor(648, 493))
            elif self.data == 3:#Disbaling the server
                print("If this was set up we would disable the server")
            else:
                #TODO: log invalid request
                print("Invalid request")
                self.request.sendall("STRING INVALID\n")
            print("Past if loop, continuing on")

if __name__ == "__main__":
    print("Running")
    HOST, PORT = "chaoticpi.local", 9999

    server = SocketServer.TCPServer((HOST, PORT), RequestHandler)

    while(True):
        server.handle_request()
        print("Past first request handle")
        server.handle_request()
        print("Past second request handle")
    print("Past serve_forever call")