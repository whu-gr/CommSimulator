import rospy
import numpy as np
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import mitsuba as mi
from instant_rm import MapTracer
from functools import partial

rospy.init_node('rss_map_node')
robot_id = rospy.get_param('~robot_id', 'wheeled0')
print("robot " + robot_id + " initiated!")
# Load the scene
# Initialize the CvBridge
bridge = CvBridge()
import os
def tx_position_callback(msg):
    timestamp = msg.header.stamp.to_sec()
    os.system(f"python3 ~/CommSimulator/src/rss_map_processor/src/rss_predict_ros.py {robot_id} {msg.point.x} {msg.point.y} {timestamp}")

rospy.Subscriber(robot_id + '/position', PointStamped, tx_position_callback)
rospy.spin()