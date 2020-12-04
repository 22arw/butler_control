#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def callback(data):
    pub = rospy.Publisher('/diff_drive_ctrl/cmd_vel', Twist, queue_size=10)
    pub.publish(data)

def listener():
    rospy.init_node("remap", anonymous=False)
    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()