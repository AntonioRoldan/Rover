#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Point
from ar_track_alvar_msgs.msg import AlvarMarker
from ar_track_alvar_msgs.msg import AlvarMarkers
import tf2_ros
from std_msgs.msg import Int32

rospy.init_node('node_listener') #init node

#listener = tf.TransformListener() #setup tf listener
tfBuffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tfBuffer)

rate = rospy.Rate(10.0) #set spin rate to 10 Hz
#pub = rospy.Publisher('/marker_id', Point, queue_size=1)
pub = rospy.Publisher('/marker_xy', Point, queue_size=1)
idpub = rospy.Publisher('/marker_id', Int32, queue_size=1)

def callback(data):
	for val in data.markers:

		idpub.publish(val.id)
		if val.id == 1:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_1', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 2:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_2', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 3:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_3', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 4:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_4', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 5:
                        trans = tfBuffer.lookup_transform('map', 'ar_marker_5', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 6:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_6', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 7:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_7', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 8:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_8', rospy.Time(), rospy.Duration(10.0))
		elif val.id == 9:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_9', rospy.Time(), rospy.Duration(10.0))
		else:
			trans = tfBuffer.lookup_transform('map', 'ar_marker_10', rospy.Time(), rospy.Duration(10.0))
		#Point point
		#point.x = trans.transform.translation.x
		#point.y = trans.transform.translation.y
		#point.z = trans.transform.translation.z
		pub.publish(trans.transform.translation)



rospy.Subscriber('/ar_pose_marker', AlvarMarkers, callback)
rospy.spin()
