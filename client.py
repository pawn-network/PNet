from pnclient import PNClient
from pnpacket import PNPacket

pkt = PNPacket(1, name='Louzin', age=17)

client = PNClient('127.0.0.1', 3030)

if __name__ == '__main__':
    client.send(pkt)