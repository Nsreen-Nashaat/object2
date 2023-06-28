#!/usr/bin/env python3
import rospy
import sys
import csv
import os
import moveit_commander
import moveit_msgs.msg as msg
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from math import pi

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def callback1(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[0] == 1) :
        with open('filex.csv','a') as csv_file:
            flags[0] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 1"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 1 saved successfuly")
            rospy.sleep(2)

def callback2(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[1] == 1) :
        with open('filex.csv','a') as csv_file:
            flags[1] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 2"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 2 saved successfuly")
            rospy.sleep(2)

def callback3(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[2] == 1) :
        with open('filex.csv','a') as csv_file:
            flags[2] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 3"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 3 saved successfuly")
            rospy.sleep(2)

def callback4(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[3] == 1):
        with open('filex.csv','a') as csv_file:
            flags[3] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 4"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 4 saved successfuly")
            rospy.sleep(2)
'''
def callback5(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[4] == 1):
        with open('filex.csv','a') as csv_file:
            flags[4] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 5"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 5 saved successfuly")
            rospy.sleep(2)

def callback6(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[6] == 1):
        with open('filex.csv','a') as csv_file:
            flags[6] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 6"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 6 saved successfuly")
            rospy.sleep(2)

def callback7(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[6] == 1):
        with open('filex.csv','a') as csv_file:
            flags[6] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 7"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 7 saved successfuly")
            rospy.sleep(2)

def callback8(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[7] == 1):
        with open('filex.csv','a') as csv_file:
            flags[7] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 8"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 8 saved successfuly")
            rospy.sleep(2)

def callback9(msg):
    #target.pose.position.x = msg.pose.position.x
    if (flags[8] == 1):
        with open('filex.csv','a') as csv_file:
            flags[8] = 0
            csv_writer = csv.writer(csv_file,delimiter = ',')
            csv_writer.writerow(["ID = 9"])
            csv_writer.writerow([msg.pose.position])
            print ("ID 9 saved successfuly")
            rospy.sleep(2)
    
'''
def save_pos():
    target = PoseStamped()
    sub1 = rospy.Subscriber("/aruco_single1/pose", PoseStamped, callback1)
    rospy.sleep(2)
    sub2 = rospy.Subscriber("/aruco_single2/pose", PoseStamped, callback2)
    rospy.sleep(2)
    sub3 = rospy.Subscriber("/aruco_single3/pose", PoseStamped, callback3)
    rospy.sleep(2)
    sub4 = rospy.Subscriber("/aruco_single4/pose", PoseStamped, callback4)
    rospy.sleep(2)

    '''
    sub5 = rospy.Subscriber("/aruco_single5/pose", PoseStamped, callback5)
    rospy.sleep(2)
    sub6 = rospy.Subscriber("/aruco_single6/pose", PoseStamped, callback6)
    rospy.sleep(2)
    sub7 = rospy.Subscriber("/aruco_single7/pose", PoseStamped, callback7)
    rospy.sleep(2)
    sub8 = rospy.Subscriber("/aruco_single8/pose", PoseStamped, callback8)
    rospy.sleep(2)
    sub9 = rospy.Subscriber("/aruco_single9/pose", PoseStamped, callback9)
    rospy.sleep(2)
    '''
    n = rospy.get_param('~sw_num')
def get_pos(n): # n is id of switch 
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

def start():
    target = PoseStamped()
    target.header.frame_id = "base_link"

    rospy.init_node("moveit_press_node", anonymous = True)

    moveit_commander.roscpp_initialize(sys.argv)

    robot = moveit_commander.robot.RobotCommander()

    moveit_gp = moveit_commander.MoveGroupCommander("manipulator")
    hand = moveit_commander.MoveGroupCommander("gripper")

    moveit_gp.set_pose_reference_frame("base_link")
    moveit_gp.set_end_effector_link("tool0")
    moveit_gp.set_goal_position_tolerance(0.005)
    moveit_gp.allow_replanning(True)

    pub = rospy.Publisher("/move_group/display_planned_path",msg.DisplayTrajectory,queue_size=20)

    home = [0,-2*pi/3,5*pi/9,pi/9,pi/2,-pi/2]
    moveit_gp.go(home, wait=True)

    end_effector_link = "tool0"
    start_pos = moveit_gp.get_current_pose(end_effector_link).pose

    target.pose.orientation.x = start_pos.orientation.x
    target.pose.orientation.y = start_pos.orientation.y
    target.pose.orientation.z = start_pos.orientation.z
    target.pose.orientation.w = start_pos.orientation.w

    print("Home Position now")

    moveit_gp.go(home, wait=True)
    rospy.sleep (2)
    print("Home Position now")

    global flags
    flags = [1,1,1,1]
    #flags = [1,1,1,1,1,1,1,1,1] 
    with open('filex.csv','w') as csv_file:
        x = input ("Enter 3 to start ")
        while (x == "3"):
            save_pos()
            if (sum(flags) == 0):
                break
        print ("Positions Saved")

    moveit_gp.go(home, wait=True)
    print ("Home Position now")
    rospy.sleep(2)

    # here i tried to close switch 3 after saving positions
    cpos = get_pos(1)
    target.pose.position.x = float(cpos[0])-0.25 + 0.015
    target.pose.position.y = float(cpos[1])
    target.pose.position.z = float(cpos[2]) -(0.025 + 0.03)
    
    (plan,_)= moveit_gp.compute_cartesian_path([target.pose],0.01,0)
    moveit_gp.execute(plan, wait=True)
    print("switch 1 pressed successfully")
    rospy.sleep(2)

# start here
start()
    