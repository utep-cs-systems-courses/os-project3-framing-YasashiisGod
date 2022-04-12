import os
import socket
from lab.fSocket import FramingSocket
from lib import params


def savetoFiles(contentList):
    os.chdir("server")
    directory = os.getcwd()

    for content in contentList:
        fileCount = len(os.listdir(directory))

        print(fileCount)

        fileName = "file" + str(fileCount + 1) + ".txt"

        open(fileName, "x")

        # write to file
        with open(fileName, "w") as outFile:
            outFile.write(content)


def runServer():
    switchVarDefault = ((('-l', "listenPort"), "listenPort", 50001),)
    paramMap = params.parseParams(switchVarDefault)
    listenPort = paramMap["listenPort"]
    listenAddr = ''  # symbolic name meaning all available interfaces

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create listening socket
    s.bind((listenAddr, listenPort))  # bind socket to address (READY TO LISTEN AT A LOC)
    s.listen(5)  # Allows 5 connections

    while 1:
        conn, addr = s.accept()  # accept incoming request
        fr = FramingSocket(conn)


runServer()
