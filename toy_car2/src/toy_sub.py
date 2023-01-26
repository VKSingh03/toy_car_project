#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

class  Sub:
    def __init__(self):
        self.steer_angle=0.0
        self.vel_cmd=0.0

    def update_steer(self,data):
        self.steer_angle= data.data
        

    def update_velocity(self,data):
        self.vel_cmd= data.data

    def subsciber(self):
        
        pub_right = rospy.Publisher('/toy_car2/joint1_position_controller/command', Float64, queue_size=10)
        pub_left = rospy.Publisher('/toy_car2/joint2_position_controller/command', Float64, queue_size=10)
        pub_move1 = rospy.Publisher('/toy_car2/joint3_position_controller/command', Float64, queue_size=10) 
        pub_move2 = rospy.Publisher('/toy_car2/joint4_position_controller/command', Float64, queue_size=10)
        rospy.init_node('subscriber', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        rospy.Subscriber("/toy_car2/steering", Float64, self.update_steer)
        rospy.Subscriber("/toy_car2/velocity", Float64, self.update_velocity)

        while not rospy.is_shutdown():
            data_str = "Velocity %s " % self.vel_cmd +"Steer Angle %s" % self.steer_angle
            rospy.loginfo(data_str)
            pub_right.publish(self.steer_angle)
            pub_left.publish(self.steer_angle)
            pub_move1.publish(self.vel_cmd)
            pub_move2.publish(self.vel_cmd)
            rate.sleep()

if __name__ == '__main__':
    try:
        s=Sub()
        s.subsciber()
    except rospy.ROSInterruptException:
        pass