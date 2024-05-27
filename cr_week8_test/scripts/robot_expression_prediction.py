#!/usr/bin/env python
from __future__ import print_function
import rospy
from cr_week8_test.msg import *
from bayesian.bbn import *
import imp; imp.find_module('bayesian_belief_networks')
from bayesian_belief_networks.ros_utils import *

def f_object_size(object_size):
	return 0.5

def f_human_action(human_action):
	return 1.0/3

def f_human_expression(human_expression):
	return 1.0/3

def f_robot_expression(robot_expression, object_size, human_action, human_expression):
	O = object_size
	HA = human_action
	HE = human_expression
	RE = robot_expression
	table = dict()
	table['HRSH'] = 0.8
	table['HRSS'] = 0.2
	table['HRSN'] = 0.0
	table['HRBH'] = 1.0
	table['HRBS'] = 0.0
	table['HRBN'] = 0.0
	table['HOSH'] = 0.8
	table['HOSS'] = 0.2
	table['HOSN'] = 0.0
	table['HOBH'] = 1.0
	table['HOBS'] = 0.0
	table['HOBN'] = 0.0
	table['HASH'] = 0.6
	table['HASS'] = 0.2
	table['HASN'] = 0.2
	table['HABH'] = 0.8
	table['HABS'] = 0.2
	table['HABN'] = 0.0

	table['SRSH'] = 0.0
	table['SRSS'] = 0.0
	table['SRSN'] = 1.0
	table['SRBH'] = 0.0
	table['SRBS'] = 0.0
	table['SRBN'] = 1.0
	table['SOSH'] = 0.0
	table['SOSS'] = 0.1
	table['SOSN'] = 1.0
	table['SOBH'] = 0.1
	table['SOBS'] = 0.1
	table['SOBN'] = 0.8
	table['SASH'] = 0.0
	table['SASS'] = 0.2
	table['SASN'] = 0.8
	table['SABH'] = 0.2
	table['SABS'] = 0.2
	table['SABN'] = 0.6

	table['NRSH'] = 0.7
	table['NRSS'] = 0.3
	table['NRSN'] = 0.0
	table['NRBH'] = 0.8
	table['NRBS'] = 0.2
	table['NRBN'] = 0.0
	table['NOSH'] = 0.8
	table['NOSS'] = 0.2
	table['NOSN'] = 0.0
	table['NOBH'] = 0.9
	table['NOBS'] = 0.1
	table['NOBN'] = 0.0
	table['NASH'] = 0.6
	table['NASS'] = 0.2
	table['NASN'] = 0.2
	table['NABH'] = 0.7
	table['NABS'] = 0.2
	table['NABN'] = 0.1

	key = ''
	key = key + 'H' if HE == '1' else key + 'S' if HE == '2' else key + 'N'
	key = key + 'R' if HA == '1' else key + 'O' if HA == '2' else key + 'A'
	key = key + 'S' if O == '1' else key + 'B'
	key = key + 'H' if RE == '1' else key + 'S' if RE == '2' else key + 'N'
	return table[key]

def robot_expression_prediction():
	rospy.init_node('robot_expression_prediction')
	g = ros_build_bbn(
		f_object_size,
		f_human_action,
		f_human_expression,
		f_robot_expression,
		domains=dict(
			object_size=['1', '2'],
			human_action=['1', '2', '3'],
			human_expression=['1', '2', '3'],
			robot_expression=['1', '2', '3']))

	rospy.spin()

if __name__ == '__main__':
	try:
		robot_expression_prediction()
	except rospy.ROSInterruptException():
		pass

