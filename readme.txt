Folder in ZIP folder: 
1. Solidworks parts and assembly : Contains all the parts and final assembly with mates, axes and global origin.
2. toy_car2 : The final package for the project. 
3. URDF from Solidworks : Contains the URDF, launch files and meshes generated from the Solidworks urdf export plugin. 
4. vsingh03_project_report.pdf : The project 1 report file. 


# Packages needed: 
1. ros_control 
2. toy_car2

# Run below command in catkin_ws after moving the toy_car2 package in catkin_ws 
$ catkin_make

# Run the template_launch file using below command to launch the robot in gazebo.
$ roslaunch toy_car2 final.launch

# RVIZ is included as part of final launch file and should Run the RVIZ on launch. If it does not open, then use below command for opening Rviz. 
$ rviz rviz

# Robot control using Teleop 
$rosrun toy_car2 teleop.py
# Now use the keys to control the car movement. 

# Close the teleop operation. 


# Robot control using Publisher and Subscriber 
# Run the publisher command. 
$ rosrun toy_car2 toy_pub.py

# Run the subscriber in a separate terminal
$ rosrun toy_car2 toy_sub.py
# After this the car will trace a circle in Gazebo.


# To check the publisher and subscriber nodes: 
$rostopic list 
# Topics of Interest - toy_car2/steering , toy_car2/velocity


# To see the data being published on these topics
$ rostopic echo toy_car2/steering 
$ rostopic echo toy_car2/velocity


# To check the nodes mapping in rqt_graph. 
$ rosrun rqt_graph rqt_graph

