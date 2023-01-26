#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def publisher():
    pub_steer = rospy.Publisher('/toy_car2/steering', Float64, queue_size=10) 
    pub_move = rospy.Publisher('/toy_car2/velocity', Float64, queue_size=10) 
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        data_str = "Pubishing Commands to Topics"
        rospy.loginfo(data_str)
        pub_steer.publish(0.5)
        pub_move.publish(5)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass