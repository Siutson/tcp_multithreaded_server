import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

print('Waiting for connection response')

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))


res = ClientMultiSocket.recv(1024)
dataToSend = 1

while True:
    ClientMultiSocket.send(dataToSend.to_bytes(2, byteorder='big'))
    res = ClientMultiSocket.recv(1024)

    print('Message from server:\n')
    encodedData = int.from_bytes(res, byteorder='big')
    print(f"Otrzymano {encodedData!r}")
    dataToSend += 1
ClientMultiSocket.close()