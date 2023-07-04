from socket import socket, AF_INET, SOCK_DGRAM
from pnpacket import PNPacket

class PNClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock_fd = socket(AF_INET, SOCK_DGRAM)

    def send(self, pnPacket: PNPacket):
        strPkt = pnPacket.stringfy()
        self.sock_fd.sendto(strPkt.encode(), (self.host, self.port))
