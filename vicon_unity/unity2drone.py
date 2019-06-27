#!/usr/bin/env python

import rospy
from drone import Drone

import os
from socket import *

from multiprocessing import Process


host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)


def wait_for_msg():
	print "Waiting to receive messages..."
	while True:
	    (data, addr) = UDPSock.recvfrom(buf)
	    print "Received message: " + data
	    if data == "exit":
	        break
	UDPSock.close()
	os._exit(0)


rospy.init_node('drone_control', anonymous=True)

pose_recording = Process(target=wait_for_msg)
pose_recording.start()

drone = Drone()

drone.arm()
drone.takeoff(1.0)
drone.hover(1.0)

drone.land()

