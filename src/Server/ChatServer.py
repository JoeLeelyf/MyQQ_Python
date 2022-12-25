import socket
import threading
import queue
import json
import time

class ChatServer(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.clients = []
        self.clients_dict={}
        self.messages = queue.Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(50)
        self.start()

    def run(self):
        while True:
            client, address = self.socket.accept()
            rec = json.loads(client.recv(1024))
            print(rec)
            print(client)
            u_id = rec['u_id']
            self.send_to_all(bytes(f"{u_id} has joined the chat", "utf-8"),rec['UorG'],rec['u_id'],rec['r_id'])
            self.clients.append((rec,client),)
            print(self.clients)
            threading.Thread(target=self.handle_client, args=(client,rec['UorG'],rec['u_id'],rec['r_id'])).start()

    def handle_client(self, client,UorG,s_id,r_id):
        while True:
            try:
                data = client.recv(1024)
                mes=[UorG,s_id,r_id,data]
                if data:
                    if data.decode("utf-8") == ":wq":
                        self.send_to_all(bytes(f"{s_id} has left the chat", "utf-8"),UorG,s_id,r_id)
                        client.close()
                        return False
                    self.messages.put(mes)
            except:
                self.send_to_all(bytes(f"{s_id} has left the chat", "utf-8"),UorG,s_id,r_id)
                client.close()
                return False

    def send_to_all(self, message, UorG ,s_id,r_id):
        for client_dic in self.clients:
            if client_dic[0]['UorG'] == 'U' and client_dic[0]['r_id'] == s_id:
                print(message)
                client_dic[1].send(message)
                time.sleep(0.1)
            elif client_dic[0]['UorG'] == 'G' and client_dic[0]['r_id'] == r_id:
                client_dic[1].send(message)
                time.sleep(0.1)
            

    def broadcast(self):
        while True:
            if not self.messages.empty():
                message = self.messages.get()
                print(message)
                data=bytes((str(message[1])+": "),"utf-8")+message[3]
                self.send_to_all(data,message[0],message[1],message[2])

    def __del__(self):
        self.socket.close()
    
if __name__ == "__main__":
    server = ChatServer("localhost", 8080)
    server.broadcast()
    
                        
    