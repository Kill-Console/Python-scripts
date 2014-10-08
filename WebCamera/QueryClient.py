# -*- coding: UTF-8 -*-

import socket
import time

ser_address = ('10.13.29.28', 10218)
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cli_socket.settimeout(5)

# send messages to server, if timeout, resend
while 1:
    cli_socket.sendto('query', ser_address)
    try:
        message, address = cli_socket.recvfrom(2048)
        if len(message):
            message_gbk = message.decode('gbk')
            print message_gbk
            break
    except socket.timeout:
        continue

time.sleep(20)
