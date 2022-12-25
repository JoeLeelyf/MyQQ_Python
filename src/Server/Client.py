import socket
import threading
import json

class Client:
    def __init__(self, u_id,UorG,r_id):
        self.u_id = u_id
        self.UorG = UorG
        self.r_id = r_id
        send={}
        send['u_id']=u_id
        send['UorG']=UorG
        send['r_id']=r_id
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("localhost", 8080))
        self.socket.send(bytes(json.dumps(send), "utf-8"))
        threading.Thread(target=self.receive).start()

    def receive(self):
        while True:
            try:
                data = self.socket.recv(1024).decode("utf-8")
                if data:
                    print(data)
            except:
                self.socket.close()
                return False

    def sendMessage(self, message):
        self.socket.send(message.encode("utf-8"))
    


