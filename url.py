#!/usr/bin/python

################################
#just for test urllib2
#2015.5
##################################

import os
import time
import socket
import httplib

def url_request(s_url, agent, port):
    conn = httplib.HTTPConnection(agent, port) 
    conn.request('GET',s_url)
    conn.close()

def raw_url_request(s_url, agent, port):
    pass

def cc_url(s_url, agent_list):
    pass


