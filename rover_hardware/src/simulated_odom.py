#!/usr/bin/env python
import rospy
import tf
import math
br = tf.TransformBroadcaster()
cnt = 0
position_rover = [0.,0.]
def calculate_position():
	global cnt
	if cnt > 300:
		cnt = 0
	cnt = cnt+1
	x = 3* math.cos(cnt*0.02)
	y = math.sin(2*cnt*0.02)
	position = (x,y)
	return position
if __name__ == '__main__':
	rospy.init_node("dynamic_tf_broadcaster")
	rate = rospy.Rate(100)
	while not rospy.is_shutdown():
		#getting actual position
		position_rover = calculate_position()
		#broadcasting transform
		br.sendTransform((position_rover[0], position_rover[1],0),
						  tf.transformations.quaternion_from_euler(0,0,0),
						  rospy.Time.now(), "base_footprint", "odom")
		rate.sleep()
