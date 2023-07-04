import socket
import threading
import pnpacket

class PNServer:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.sock_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.shutdown = False
        self.listening = False

    def thread_listener(self, callback=None, **kwargs):
        while True and self.shutdown is False:
            packet, client = self.sock_fd.recvfrom(1024) 
            if packet is not None:
                pnPkt = pnpacket.PNPacket.fromStr(packet.decode())
                callback(pnPkt, client, **kwargs)
    
    def shutdown(self):
        self.shutdown = True

    def listen(self, callback=None, **kwargs):
        if self.shutdown is True:
            self.shutdown = False
        if self.listening is False:
            self.sock_fd.bind((self.host, self.port))
            thread = threading.Thread(target=self.thread_listener, args=(callback,), kwargs=(kwargs))
            thread.start()
            self.listening = True
