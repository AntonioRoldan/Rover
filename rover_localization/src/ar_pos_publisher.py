#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Point

rospy.init_node('node_listener') #init node

listener = tf.TransformListener() #setup tf listener

rate = rospy.Rate(10.0) #set spin rate to 10 Hz
pub = rospy.Publisher('/marker_id', Point, queue_size=1)
rospy.Subscriber('/ar_pose_marker', Twist, callback)

while not rospy.is_shutdown():
    #lookup for the newest transform
    try:
        
        (trans,rot)=listener.lookupTransform('/map', '/ar_marker_8',
                                             rospy.Time(0))
            
            
            #get euler angles form quaternions
            euler =tf.transformations.euler_from_quaternion(rot)
                
                #print translation and rotation
                pub.publish(trans)
                                             except (tf.LookupException, tf.ConnectivityException,
                                                     tf.ExtrapolationException):
                                                 pass
                                                     rate.sleep()
