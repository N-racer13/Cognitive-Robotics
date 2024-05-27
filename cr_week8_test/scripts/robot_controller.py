#!/usr/bin/env python
from __future__ import print_function
import rospy
from cr_week8_test.msg import *
from bayesian.bbn import *
import imp; imp.find_module('bayesian_belief_networks')
from bayesian_belief_networks.ros_utils import *
from bayesian_belief_networks.srv import Query
from bayesian_belief_networks.msg import Observation

def callback(info):
	rospy.wait_for_service('robot_expression_prediction/query')
	try:
		query = rospy.ServiceProxy('robot_expression_prediction/query', Query)
		msg = []
		O = info.object_size
		HA = info.human_action
		HE = info.human_expression
		if O != 0:
			obs = Observation('object_size', str(O))
			msg.append(obs)
		if HA != 0:
			obs = Observation('human_action', str(HA))
			msg.append(obs)
		if HE != 0:
			obs = Observation('human_expression', str(HE))
			msg.append(obs)
		resp = query(msg)
		p_value = [0, 0, 0]
		expression_list = [res for res in resp.results if res.node == 'robot_expression']
		for i in expression_list:
			p_value[int(i.Value)-1] = i.Marginal
		pub = rospy.Publisher('robot_info', robot_info, queue_size = 10)
		pub.publish(info.ID, p_value[0], p_value[1], p_value[2])
	except:
		pass


def robot_controller():
	rospy.init_node('robot_controller', anonymous=True)
	rospy.Subscriber('perceived_info', perceived_info, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		robot_controller()
	except rospy.ROSInterruptException():
		pass
		robot_controller()
	except rospy.ROSInterruptException():
		pass
