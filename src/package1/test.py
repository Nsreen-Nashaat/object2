#!/usr/bin/env python3
import csv
import os
import rospy 
import moveit_commander
import moveit_msgs
import sys

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('aruco_pos',anonymous=True)
move_group = moveit_commander.MoveGroupCommander('manipulator')
display_trajectory_publisher = rospy.Publisher(
            "/move_group/display_planned_path",
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=20,
        )

os.chdir(os.path.dirname(os.path.abspath(__file__)))
n = rospy.get_param('~sw_num')
rospy.loginfo(n)
def get_pos(n):
    with open('filex.csv','r') as csv_pos_file: 
        csv_reader = csv.reader(csv_pos_file)
        y=[] 
        pos=[]
        for line in csv_reader : #read file
            for word in line :   
                y.append (word) #move elements to list y
        i=0
        for key in y : 
            i += 1
            if key == f"ID = {n}":  #search in list for ID n
                y[i]= y[i].split()
                pos.append(y[i][1]) #add position to new list pos
                pos.append(y[i][3])
                pos.append(y[i][5])
                break        
        return pos 
##print(get_pos(3))


