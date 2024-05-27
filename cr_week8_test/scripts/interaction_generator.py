#!/usr/bin/env python
from __future__ import print_function
import rospy
import random
from cr_week8_test.msg import human_info, object_info

def interaction_generator():
	rospy.init_node('generator', anonymous=True)
	pub1 = rospy.Publisher('object_info', object_info, queue_size=10)
	pub2 = rospy.Publisher('human_info', human_info, queue_size=10)
	ID = 0
	rate = rospy.Rate(0.1)
	while not rospy.is_shutdown():
		ID += 1
		object_size = random.randint(1, 2)
		human_action = random.randint(1, 3)
		human_expression = random.randint(1, 3)
		pub1.publish(ID, object_size)
		pub2.publish(ID, human_action, human_expression)
		rate.sleep()
		print("ID: " + str(ID))
		print("object size: " + str(object_size))
		print("human action: " + str(human_action))
		print("human expression: " + str(human_expression))

if __name__ == '__main__':
	try:
		interaction_generator()
	except rospy.ROSInterruptException():
		pass
