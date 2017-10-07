#!/usr/bin/env python
import roslib
import rospy
import tf

from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion

br = tf.TransformBroadcaster()
quat = Quaternion()

def publishTransform():
	global quat

	rot = (quat.x, quat.y, quat.z, quat.w)
	(roll, pitch, yaw) = tf.transformations.euler_from_quaternion(rot)
	
	br.sendTransform((0,0,0),
		tf.transformations.quaternion_from_euler(roll,pitch,yaw),
		rospy.Time.now(),
		"base_footprint”,
		“attitude")

def callback(data):
	global quat
	quat = data.orientation
	publishTransform()

if __name__ == '__main__':
	rospy.init_node('tf_broadcaster')
	rospy.Subscriber("/imu/data", Imu, callback)
	rospy.spin()
