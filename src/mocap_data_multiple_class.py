#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Quaternion, Pose, PoseStamped
from gazebo_msgs.msg import ModelState
import numpy as np

# state0 = ModelState()
# state0.model_name = 'iris0'

# state1 = ModelState()
# state1.model_name = 'iris1'

# state2 = ModelState()
# state2.model_name = 'iris2'
n_drones = 3

class Drone:
    def __init__(self,id):
        self.id = id
        self.state = ModelState()
        self.state.model_name = 'iris' + str(id)
        self.pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
        self.sub = rospy.Subscriber("/qualisys_node/cf" + str(id) + "/pose", PoseStamped, self.callback)        

    def callback(self,data):
        self.state.pose = data.pose     

if __name__ == '__main__':
    rospy.init_node('mocap_data_multiple', anonymous=True)
    rate = rospy.Rate(100) 
    # pub0 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
    # pub1 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
    # pub2 = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)        

    # rospy.Subscriber("/qualisys_node/cf0/pose", PoseStamped, callback_0)
    # rospy.Subscriber("/qualisys_node/cf1/pose", PoseStamped, callback_1)
    # rospy.Subscriber("/qualisys_node/cf2/pose", PoseStamped, callback_2)

    objs = list()
    for i in range(n_drones):
        objs.append(Drone(i))

    # for i in range(n_drones):
    #     drone_name = 'drone' + str(i)


    while not rospy.is_shutdown():
        # pub0.publish(state0)
        # pub1.publish(state1)
        # pub2.publish(state2)
        for i in range(n_drones):
            objs[i].pub.publish(objs[i].state)
        
        rate.sleep()
    # while not rospy.is_shutdown():
    #     for id in range(n_drones):
    #         drone_name = 'drone' + str(id)
    #         drone_name = Drone(id)
    #         drone_name.publish_data()



    
    
   