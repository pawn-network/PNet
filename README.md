# PNet

    Em breve, tutorial de uso.

## PNPackets

    PNPackets são pacotes JSON ( dicts ) que podem ser criados e manipulados dinamicamente.

    - packetId:
      - Todo PNPacket tem um ID, para indentificar qual o pacote em suas aplicações.
      - Podemos criar então os pacotes, e enviar ao servidor, o servidor vai tratar esses pacotes de acordo com seu PacketID.

    - jData:
      - Informações do Packet

    - Criando um PNPacket:

### Criando um PNPacket

```py
from PNet import PNPacket
PACKET_ID_USER = 2 # ID do nosso PNPacket User.
PACKET_ID_CAR = 3 # ID do nosso PNPacket Car
pkt = PNPacket(PACKET_ID_USER, username='Krieger', password='1234')
'''
    Isso vai criar um pacote de id 2, com o JSON assim:

    {
        "username": "Krieger",
        "password": 1234
    }
'''

pkt2 = PNPacket(PACKET_ID_CAR, carname='Civic', age=3)
'''
    Vai criar um pacote de id 3, com o JSON assim:

    {
        "car": "Civic",
        "age": 3
    }
'''
```

## PNServer

    PNServer é a classe do servidor PNet.

### Criando um PNServer

```py
from PNet import PNPacket
from PNet import PNServer

server = PNServer('127.0.0.1', 3030) # Criando o servidor

# Criando a callback para tratar os pacotes recebidos.
def callback(pnPacket, client, **kwargs):
    packetId = pnPacket.getPacketId()
    data = pnPacket.getJSONData()

    if packetId == PACKET_ID_USER: # caso o ID seja o id PACKET_ID_USER do nosso exemplo acima
        print(f"Pacote de usuario recebido.\nUsername: {data.get('username')}\nPassword: {data.get('password')}")
    elif packetId == PACKET_ID_CAR: # caso o ID seja o id PACKET_ID_CAR do nosso exemplo acima
        print(f"Pacote de carro recebido.\nModelo: {data.get('carname')}\nIdade: {data.get('age')}")
    else:
        print(f"Pacote desconhecido recebido.")

server.listen(callback) # Você pode usar KWARGS caso precise tambem.

```

## PNClient

    PNClient é a classe do client PNet.

### Criando um PNClient

```py
from PNet import PNPacket
from PNet import PNClient

client = PNClient('127.0.0.1', 3030) # endereço do nosso PNServer.

client.send(pkt) # Enviando o pacote que criamos
client.send(pkt2) # Enviando o outro pacote que criamos
```
