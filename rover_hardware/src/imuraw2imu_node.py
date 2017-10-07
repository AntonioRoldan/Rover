#!/usr/bin/env python

import roslib
import rospy

from crius_imu.msg import ImuMin
from sensor_msgs.msg import Imu

rospy.init_node('imuraw2imu_node')

imu_msg = Imu()

imu_msg.orientation_covariance = (1.0, 0, 0,
					0, 1.0, 0,
					0, 0, 1.0)
imu_msg.angular_velocity_covariance = (1.25e-07, 0, 0,
						0, 1.25e-07, 0,
						0, 0, 1.25e-07)
imu_msg.linear_acceleration_covariance = (8.99e-08, 0, 0,
						0, 8.99e-08, 0,
						0, 0, 8.99e-08)

pub = rospy.Publisher('/imu/data', Imu, queue_size=1)

def callback(data):

	imu_msg.header.stamp = rospy.get_rostime()
	imu_msg.header.frame_id = "imu"

	imu_msg.orientation.x = data.quat_x
	imu_msg.orientation.y = data.quat_y
	imu_msg.orientation.z = data.quat_z
	imu_msg.orientation.w = data.quat_w

	imu_msg.angular_velocity.x = data.gyro_x
	imu_msg.angular_velocity.y = data.gyro_y
	imu_msg.angular_velocity.z = data.gyro_z

	imu_msg.linear_acceleration.x = data.acc_x
	imu_msg.linear_acceleration.y = data.acc_y
	imu_msg.linear_acceleration.z = data.acc_z
	
	pub.publish(imu_msg)


rospy.Subscriber("/imu/raw_data", ImuMin, callback)

rospy.spin()
