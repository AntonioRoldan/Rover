#!/usr/bin/env python

################### import ###########################
import rospy
from std_msgs.msg import String		#keyboard cmd message type
from geometry_msgs.msg import Twist	#turtle cmd_vel message type
import tf


############# node initialization ####################
rospy.init_node('follower', anonymous=True)


distance_thresh = rospy.get_param('distance_topic', '/distance_threshold')

listener = tf.TransformListener()   #setup tf listener



############ definitions of functions ##################

def accelerate(move):
	#TODO

def deaccelerate(move):
	#TODO

def steerLeft(move):
	#TODO

def steerRight(move):
	#TODO

def callback(trans,rot):


	move = Twist()

	# adjust the forward velocity accordingly to the distance of the ar tag
	if (trans.x > distance_thresh * 1.1):
		move = accelerate(move)
		#move.linear.x = msg.axes[1]
	if (trans.x < distance_thresh * 0.9):
		move = deaccelerate(move)

	# adjust the steering accordingly to the postition of the ar tag
	if (trans.y < -0.1):
		move = steerLeft(move)
	if (trans.y > 0.1):
		move = steerRight(move)
	#move.angular.z = msg.axes[0]
	pub.publish(move)



#### definition of publisher/subscriber and services ###
(trans,rot)=listener.lookupTransform('/camera_link', '/ar_marker_8',
rospy.Time(0))
callback(trans,rot)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

############# main program #############################
#--------------endless loop till shut down -------------#
rospy.spin()
