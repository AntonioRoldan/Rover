#!/usr/bin/env python

################### import ###########################
import rospy
from std_msgs.msg import String		#keyboard cmd message type
from geometry_msgs.msg import Pose2D


############# node initialization ####################
rospy.init_node('current_pos', anonymous=True)



############ definitions of functions ##################

def callback(pos):
	try:
		pub.publish(pos)
	except rospy.ROSInterruptException:
		pass


#### definition of publisher/subscriber and services ###
pub = rospy.Publisher('/rover_current_pose', Pose2D, queue_size=1)
rospy.Subscriber('pose2D', Pose2D, callback)

############# main program #############################
#--------------endless loop till shut down -------------#
rate = rospy.Rate(10.0)
	
rospy.spin()
