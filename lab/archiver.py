import os, re, socket, sys
import params

def archiver(files):
    byteArr = bytearray()

    for i, fileName in enumerate(files):
        path = 'files/' + fileName
        with open(path, "rb") as file:
            tmpByteArr = bytearray()
            tmpByteArr = file.read()
        if (i ==0):
            byteArr = f"{len(tmpByteArr):08d}".encode() + tmpByteArr