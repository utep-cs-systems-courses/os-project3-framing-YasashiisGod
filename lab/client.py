import socket
import sys
import re
from fSocket import *

sys.path.append("../lib")
from lib import params
from archiver import archiver


def client():
    switchesVarDefaults = (
        (('-s', "--server"), "server", "127.0.0.1:50001"),
    )
    paramMap = params.parseParams(switchesVarDefaults)

    server = paramMap["server"]

    try:
        serverHost, serverPort = re.split(':', server)
        serverPort = int(serverPort)

    except:
        print("Can't parse server : port from '%s'" % server)
        sys.exit(1)

    s = None
    for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res

        try:
            print("creating sock: af= %d,type = %d, proto=%d" % (af, socktype, proto))
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            print("error: %s" % msg)
            s = None
            continue
        # try to connect to remote socket at given address
        try:
            print("attempting to connect to %s" % repr(sa))
            s.connect(sa)
        except socket.error as msg:
            print("error: %s" % msg)
            s.close()
            s = None
            continue
        break
    if s is None:
        print("could nor open socket")
        sys.exit(1)

    while 1:
        go = input()
        if go == "go":
            archived = archiver("QOTD", "Oz", "flirt")
            print(archived)
            print("Type: ", type(archived))
            fw = FramingSocket(s)
            fw.frameWriter(archived)




client()
