# -*- coding: UTF-8 -*-

import socket
import time
import traceback
from VideoCapture import Device
import threading

# global variable
is_sending = False
cli_address = ('', 0)

# the server address and port
host = ''
port = 10218

# initialize UDP socket
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ser_socket.bind((host, port))

# receiver thread class, for receiving massages from client
class UdpReceiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
                
    def run(self):
        while not self.thread_stop:
            # change the values of the global variables after receiving massages
            global cli_address   
            global is_sending
            try:
                message, address = ser_socket.recvfrom(2048)
            except:
                traceback.print_exc()
                continue           
            if message == 'startCam':
                print 'start camera'
                is_sending = True
                cli_address = address
                ser_socket.sendto('startRcv', cli_address)                
            if message == 'quitCam':
                is_sending = False
                print 'quit camera'
            if message == 'query':
                if is_sending:
                    msg = u'老板在监视你哟！'
                    msg_gbk = msg.encode('gbk')
                    ser_socket.sendto(msg_gbk,address)
                else:
                    msg = u'放心玩儿吧，老板不在~'
                    msg_gbk = msg.encode('gbk')
                    ser_socket.sendto(msg_gbk,address)

    def stop(self):
        self.thread_stop = True

print 'Waiting for connecting...'

# create receiving thread
receiveThread = UdpReceiver()
receiveThread.setDaemon(True)           # for quitting the subthread when the main thread exits
receiveThread.start()

# initialize the camera
cam = Device()
cam.setResolution(320,240)

# the main thread to send data to client
while 1:
    if is_sending:      
        img = cam.getImage().resize((160,120))
        data = img.tostring()
        ser_socket.sendto(data, cli_address) 
        time.sleep(0.05)
    else:
        time.sleep(1)

receiveThread.stop()
ser_socket.close()
