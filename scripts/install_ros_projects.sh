#!/bin/bash

# Dependency for ARToolkit/ar_tools
sudo apt-get install -y libv4l-dev

# Install cassandra_ros and dependency project
cd ~/catkin_ws/src

# Cassandra ROS project fork, with modifications for detecting markers with AR_Pose
git clone https://github.com/guriandoro/cassandra_ros.git

# Converts between Python dictionaries and JSON to rospy messages. (needed by cassandra_ros)
git clone https://github.com/uos/rospy_message_converter.git

# AR Tools
git clone https://github.com/ar-tools/ar_tools.git
cd ..
catkin_make


# Install python packages
pip install pycassa 
pip install cql

# to avoid connection errors from pycassa module, we choose ver. 0.9.3 specifically
pip install thrift==0.9.3

sudo apt-get install -y python-qt4 

# USB Camera module for ROS
sudo apt-get install -y ros-melodic-usb-cam

## Optionally, install ARToolkit examples
## Warning: skip on environments with low disk space
#cd ~/catkin_ws/src/ar_tools/ar_pose/demo/
#./setup_demos
#roslaunch ar_pose demo_single.launch
