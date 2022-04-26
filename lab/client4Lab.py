import socket
import sys
import archiver

HEADER = 100
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!F"
# SERVER = "192.168.1.129"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def sendArchivedFiles(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while 1:
    message = input("Please type your message!\n")
    if "file:" in message:
        print("archiving to send")
        message = message[6:]
        message = message.split(" ")
        print("Message has been split")
        message = archiver.archiver(message[0], message[1], message[2])
        sendArchivedFiles(message)
        continue

    if message == DISCONNECT_MESSAGE:
        send(message)
        print("----------Goodbye!----------")
        sys.exit(1)
    send(message)
