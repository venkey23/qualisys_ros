#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Quaternion, Pose, PoseStamped
from gazebo_msgs.msg import ModelState
import numpy as np

n_drones = 6
model_name = 'iris'

class Drone:
    def __init__(self,id):
        self.id = id
        self.state = ModelState()
        self.state.model_name = model_name + str(id)
        self.pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
        self.sub = rospy.Subscriber("/qualisys_node/cf" + str(id) + "/pose", PoseStamped, self.callback)        

    def callback(self,data):
        self.state.pose.position.x = data.pose.position.x * 40
        self.state.pose.position.y = data.pose.position.y * 40
        self.state.pose.position.z = (data.pose.position.z - 0.02) * 40     

if __name__ == '__main__':
    rospy.init_node('mocap_data_multiple', anonymous=True)
    rate = rospy.Rate(10) 

    objs = list()
    for i in range(n_drones):
        objs.append(Drone(i))


    while not rospy.is_shutdown():
        for i in range(n_drones):
            objs[i].pub.publish(objs[i].state)
        
        rate.sleep()



    
    
   