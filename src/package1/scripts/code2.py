import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
n = rospy.get_param('~sw_num')
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
print(get_pos(3))

