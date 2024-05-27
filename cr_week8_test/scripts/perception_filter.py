#!/usr/bin/env python
from __future__ import print_function
import rospy
import random
from cr_week8_test.msg import *
import time
import message_filters

def callback(object_info, human_info):
	Filter = random.randint(1, 8)
	ID = object_info.ID
	object_size = object_info.object_size
	human_action = human_info.human_action
	human_expression = human_info.human_expression
	if Filter == 1:
		object_size = 0
	if Filter == 2:
		human_action = 0
	if Filter == 3:
		human_expression = 0
	if Filter == 4:
		object_size = 0
		human_action = 0
	if Filter == 5:
		object_size = 0
		human_expression = 0
	if Filter == 6:
		human_action = 0
		human_expression = 0
	if Filter == 7:
		object_size = 0
		human_action = 0
		human_expression = 0
	print(Filter)
	print("ID: " + str(ID))
	print("object size: " + str(object_size))
	print("human action: " + str(human_action))
	print("human expression: " + str(human_expression))
	pub = rospy.Publisher('perceived_info', perceived_info, queue_size=10)
	pub.publish(ID, object_size, human_action, human_expression)

def perception_filter():
	rospy.init_node('filter', anonymous=True)
	object_sub = message_filters.Subscriber('object_info', object_info)
	human_sub = message_filters.Subscriber('human_info', human_info)
	ts = message_filters.ApproximateTimeSynchronizer([object_sub, human_sub], 10, 0.1, allow_headerless=True)
	ts.registerCallback(callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		perception_filter()
	except rospy.ROSInterruptException():
		pass
