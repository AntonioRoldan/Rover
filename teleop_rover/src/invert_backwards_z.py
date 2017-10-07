#!/usr/bin/env python

################### import ###########################
import rospy
from std_msgs.msg import String		#keyboard cmd message type
from geometry_msgs.msg import Twist


############# node initialization ####################
rospy.init_node('invert_backwards_z', anonymous=True)



############ definitions of functions ##################

def callback(data):
	try:
		if data.linear.x < 0.0:
			data.angular.z = -data.angular.z
		pub.publish(data)
	except rospy.ROSInterruptException:
		pass


#### definition of publisher/subscriber and services ###
pub = rospy.Publisher('/plan_cmd_vel', Twist, queue_size=1)
rospy.Subscriber('/plan_cmd_vel_raw', Twist, callback)

############# main program #############################
#--------------endless loop till shut down -------------#
rate = rospy.Rate(10.0)
	
rospy.spin()
