#!/usr/bin/env python

import rospy
import tf

rospy.init_node('node_listener') #init node

listener = tf.TransformListener() #setup tf listener

rate = rospy.Rate(10.0) #set spin rate to 10 Hz

while not rospy.is_shutdown():
	#lookup for the newest transform
	try:
		(trans,rot)=listener.lookupTransform('/camera_link', '/ar_marker_8',
		rospy.Time(0))

		#get euler angles form quaternions
		euler =tf.transformations.euler_from_quaternion(rot)
		
		#print translation and rotation
		print 'translation: ',trans
		print 'rotation: ',euler
		print '########'
	except (tf.LookupException, tf.ConnectivityException,
			tf.ExtrapolationException):
		pass
		rate.sleep()
