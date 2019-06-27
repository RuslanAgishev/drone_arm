#! /usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import TransformStamped, PoseStamped
from math import *

import os
from socket import *


host = "192.168.1.121" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

def sender_callback(data):
	msg = data#.transform.translation.x
	print "\nSending:\n", msg
	UDPSock.sendto(str(msg), addr)

def vicon2unity():
	rospy.init_node('sender', anonymous=True)
	rospy.Subscriber('/vicon/DroneArm/DroneArm', TransformStamped, sender_callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		vicon2unity()
	except rospy.ROSInterruptException:
		pass
