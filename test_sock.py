#!/usr/bin/python

################################
#just test python socket
#################################


import socket

def test_sock():
    socks = []
    for i in range(999, -1, -1):
        socks[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks[i].setblocking(0)
        socks[i].connect("10.18.31.79", 80)


    rlist, wlist, elist = select.select(socks, socks, socks)
    for sock in wlist:
        sock.send()
    
