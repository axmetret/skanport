#!/usr/bin/python3
import socket
import sys
#20 - FTPD
#21 - FTP
#22 - SSH
#23 - Telnet
#25 - SMTP
#53 - DNS
#66 - SQL-NET
#69 - TFTP
#80 - HTTP
#81 - TOR HTTP
#135 - EPMAP
#161 - SNMP
#220 - IMAP3
#443 - HTTPS
#513 - WHO
#514 - SHELL, SYSLOG

mas = [20,21,22,23,53,66,69,80,81,135,161,220,443,513,514]
print ("SKAN-PORTS")
print (" ")
host = input('Enter name host and site: ')
print ("-----------------")
print ("Loanding________!")
print ("-----------------")

for port in mas:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        pass
    else:
        s.close
        print (host + ':' + str(port) + 'activ port')
print ("Buy")
