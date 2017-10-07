#!/usr/bin/env python

################### import ###########################
import rospy
from std_msgs.msg import String		#keyboard cmd message type
from geometry_msgs.msg import Twist	#turtle cmd_vel message type
from sensor_msgs.msg import Joy
############# creation of objects #####################

############# node initialization ####################
rospy.init_node('teleop', anonymous=True)

############ definitions of functions ##################
def callback(msg):


	move = Twist()

	move.linear.x = msg.axes[1]
	move.angular.z = msg.axes[0]
	pub.publish(move)

#### definition of publisher/subscriber and services ###
rospy.Subscriber('/joy', Joy, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

############# main program #############################
#--------------endless loop till shut down -------------#
rospy.spin()
