# -*- coding: UTF-8 -*-

import socket, time
import pygame
from pygame.locals import *
from sys import exit

# the server adrress is the IP of the server machine，initialize socket
ser_address = ('10.13.29.28', 10218)
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set timeout
cli_socket.settimeout(5)

# send messages to server, if timeout, resend
while 1:
    cli_socket.sendto('startCam', ser_address)
    try:
        message, address = cli_socket.recvfrom(2048)
        if message == 'startRcv':
            print message
            break
    except socket.timeout:
        continue

# prevent waiting for data after initialization
cli_socket.recvfrom(65536)

# initialize the video window
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Web Camera')
pygame.display.flip()

# set the time to control the frame rate
clock = pygame.time.Clock()

# get the data from server and show the video
while 1:
    try:
        data, address = cli_socket.recvfrom(65536)
    except socket.timeout:
        continue
    camshot = pygame.image.frombuffer(data, (160,120), 'RGB')
    camshot = pygame.transform.scale(camshot, (640, 480))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cli_socket.sendto('quitCam', ser_address)
            cli_socket.close()
            pygame.quit()
            exit()
    screen.blit(camshot, (0,0))
    pygame.display.update() 
    clock.tick(20)
