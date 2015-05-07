#!/usr/bin/python

################################
#just test python socket
#################################


import socket
import select
def test_sock():
    socks = []
    rsocks = []
    for i in range(0, 1000):
        socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    for sock in socks:
        sock.setblocking(0)
        try:
            sock.connect(("10.18.31.79", 80))
        except:
            pass
    while(len(socks) or len(rsocks)):
        rlist, wlist, elist = select.select(rsocks,socks, socks)
        for sock in wlist:
            #print sock.getpeername()
            str = http_request()
            try:
                sock.send(str)
            except:
                pass
            socks.remove(sock)
            rsocks.append(sock)
    
        for sock in rlist:
            sock.close()
            rsocks.remove(sock)
        for sock in elist:
            if sock in rsocks:
                rsocks.remvoe(sock)
            if sock in socks:
                socks.remove(sock)
            sock.close()
        print(len(socks))
        print(len(rsocks))

def test_one():
    socks = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    try:
        sock.connect(("10.18.31.79", 80))
    except:
        pass

    wlist = select.select([],[sock], [])[1]
    print wlist
    for s in wlist:
        print sock
        if s == sock:
            print 123
            peername = s.getpeername()
        else:
            continue

    sock.close()


def test_poll():
    socks = []
    rsocks = []
    epoll = select.epoll()
    conn_q = {}
    read_q = {}
    request = http_request()
    for i in range(0, 1000):
        socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    for sock in socks:
        sock.setblocking(0)
        try:
            sock.connect(("10.18.31.79", 80))
        except:
            pass
        epoll.register(sock.fileno(), select.EPOLLOUT)
        conn_q[sock.fileno()] = sock

    while(len(conn_q) or len(read_q)):
        events = epoll.poll(1)
        for fileno, event in events:
            if conn_q.has_key(fileno):
                if event & select.EPOLLOUT:
                    conn_q[fileno].send(request)
                    epoll.modify(fileno, select.EPOLLIN)
                    read_q[fileno] = conn_q[fileno]
                    del conn_q[fileno]
                else:
                    print "except"
                    del conn_q[fileno]
            if read_q.has_key(fileno):
                if event & select.EPOLLIN:
                    epoll.modify(fileno,0)
                    read_q[fileno].close()
                    del read_q[fileno]
                else:
                    pass
            else:
                print "error"
                pass

def http_request():
    return "GET / HTTP/1.1\nHost:10.18.31.79\r\n\r\n" 


if __name__=="__main__":
    #test_sock()
    #test_one()
    test_poll()

