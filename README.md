## ROS implementation of robot communication simulator

This project repository a real-time simulation communication simulator integrated with ROS, supporting the Gazebo simulation environment. Users only need to predefine the antenna parameters and material information of the environment, and the RSS (Received Signal Strength) map can be calculated based on the real-time position of the TX.

### Installation

Please refer to [instantRM](https://github.com/NVlabs/instant-rm) and [mitsuba3](https://github.com/mitsuba-renderer/mitsuba3) for installation instructions.

Install [ROS Noetic](https://www.ros.org/) and use catkin tools to make this repository

Change the file paths in the code to your actual path, with the current path being `/home/docker-user`.

### How to Run

Similar to instantRM, we use XML files to define the environment, located in the /scenes folder of the project.

You can configure the antenna pattern in /src/rss_predict_ros.py. 

After the configuration, you can run the simulator by

`./home/docker-user/Commsimulator/src/rss_map_processor/launch/run_robotX.sh`

Then, the package will subscribe to rostopic `/robot_id/position` and publish the predicted RSS map at rostopic `/robot_id/rss_map_with_position`

