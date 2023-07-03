import json

class PNPacket:
    def __init__(self, packetId, jsonData, bjData = False, **kwargs):
        self.packetId = packetId
        self.jData = {}
        if bjData is True:
            self.jData = jsonData
        else:
            for k, v in kwargs.items():
                self.jData[k] = v

    def getPacketId(self):
        return self.packetId
    
    def getJsonData(self):
        return self.jData
    
    @staticmethod
    def resolvePacket(packet):
        jData: dict = json.loads(packet)
        pnPacket = PNPacket(jData.get('packetId'), jData, True)
        return pnPacket

    def stringfy(self):
        return json.dumps(self.jData)