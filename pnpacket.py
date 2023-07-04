import json

class PNPacket:
    def __init__(self, packetId, JSON=None, useJSON=False, **kwargs):
        self.packetId = packetId
        self.jData: dict = {}
        if useJSON:
            self.jData = JSON
        else:
            for k, v in kwargs.items():
                self.jData[k] = v

    @classmethod
    def fromStr(cls, string):
        jsonData: dict = json.loads(string)
        pktId = jsonData.get('packetId')
        jsonData.pop('packetId', None)
        return cls(pktId, jsonData, True)

    def getPacketId(self):
        return self.packetId
    
    def getJSONData(self):
        return self.jData

    def stringfy(self):
        return json.dumps(self.jData)