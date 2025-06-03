## ROS implementation of robot communication simulator

This project repository a real-time simulation communication simulator integrated with ROS, supporting the Gazebo simulation environment. Users only need to predefine the antenna parameters and material information of the environment, and the RSS (Received Signal Strength) map can be calculated based on the real-time position of the TX.

### Installation

Please refer to [instantRM](https://github.com/NVlabs/instant-rm) and [mitsuba3](https://github.com/mitsuba-renderer/mitsuba3) for installation instructions. We recommend using [Virtualenv](https://virtualenv.pypa.io/en/latest/) to manage Python environments. Suppose the virtual environment for InstantRM is located at `~/venv`, and Mitsuba3 is installed in `~/mitsuba3`.

Git clone this repository to folder `~/CommSimulator/src`.

Install [ROS Noetic](https://www.ros.org/) and use [catkin tools](https://catkin-tools.readthedocs.io/en/latest/) to build this repository.

Change the file paths in the python code to your actual path, with the current path being `~/`.

### How to Run

Similar to instantRM, we use XML files to define the environment, located in the /scenes folder of the project.

You can configure the antenna pattern in /src/rss_predict_ros.py. 

After the configuration, you can run the simulator by

```bash
source /opt/ros/noetic/setup.bash

source ~/venv/bin/activate --extend

source ~/mitsuba3/build/setpath.sh --extend

cd ~/CommSimulator/
source devel/setup.bash --extend

roslaunch rss_map_processor robot.launch robot_id:=robot0
```

Then, the package will subscribe to rostopic `/robot0/position` and publish the predicted RSS map at rostopic `/robot0/rss_map_with_position_repub` with 10Hz. You can launch multiple packages by changing the `robot_id`, enabling RSS prediction for multiple TXs.

