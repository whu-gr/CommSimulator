#!/bin/bash
source /opt/ros/noetic/setup.bash

source /home/docker-user/venv/bin/activate --extend

source /home/docker-user/mitsuba3/build/setpath.sh --extend

cd /home/docker-user/instantRM-ROS/
source devel/setup.bash --extend

roslaunch rss_map_processor robot.launch robot_id:=wheeled9