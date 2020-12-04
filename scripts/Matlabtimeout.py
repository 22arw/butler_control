#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Timeout():

    def __init__(self):
        rospy.init_node("matlab_timeout")
        rospy.Subscriber("/diff_drive_ctrl/cmd_vel", Twist, self.callback)
        
        self.pub_cmd = rospy.Publisher("/diff_drive_ctrl/cmd_vel", Twist, queue_size=10)
        self.timeout = 0.5

        self.timeout_message = Twist()
        self.timeout_message.linear.x = 0
        self.timeout_message.linear.y = 0
        self.timeout_message.linear.z = 0
        self.timeout_message.angular.x = 0
        self.timeout_message.angular.y = 0
        self.timeout_message.angular.z = 0


    def spin(self):

        r = rospy.Rate
        self.last_message_time = rospy.Time.now()
        self.sec_since_message = self.timeout

        while not rospy.is_shutdown():
            while not rospy.is_shutdown() and self.sec_since_message < self.timeout:
                r.sleep
                self.sec_since_message = (rospy.Time.now() - self.last_message_time).to_sec()
            self.sec_since_message = (rospy.Time.now() - self.last_message_time).to_sec()
            r.sleep
            self.pub_cmd.publish(self.timeout_message)


    def callback(self, data):
        self.last_message_time = rospy.Time.now()
                

if __name__ == '__main__':
    try:
        time = Timeout()
        time.spin()
    except rospy.ROSInterruptException:
        pass