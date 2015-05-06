#!/usr/bin env python
import socket
host="www.haosou.com"
se=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
se.connect((host,80))
se.send("GET / HTTP/1.1\n")
se.send("Accept:text/html,application/xhtml+xml,*/*;q=0.8\n")
#se.send("Accept-Encoding:gzip,deflate,sdch\n")
se.send("Accept-Language:zh-CN,zh;q=0.8,en;q=0.6\n")
se.send("Cache-Control:max-age=0\n")
se.send("Connection:keep-alive\n")
se.send("Host:"+host+"\r\n")
se.send("Referer:http://www.haosou.com/\n")
se.send("user-agent: Googlebot\n\n")
while True:
    buf = se.recv(1024)
    if not len(buf):
        break
    print buf
    se.close()
    break
