from pnpacket import PNPacket
from pnserver import PNServer

server = PNServer('127.0.0.1', 3030)

def callback(pnPacket: PNPacket, client, **kwargs):
    print(f"Packet id {pnPacket.getPacketId()}\nPacket data {pnPacket.getJSONData()}")
    for k, v in kwargs.items():
        print(f"Extra arg {k} = {v}")


if __name__ == '__main__':
    server.listen(callback, time=10, message='ola')