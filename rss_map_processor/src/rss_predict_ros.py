import sys
import rospy
import mitsuba as mi
from instant_rm import MapTracer
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import time

# robot -> instantRM: x+22;y-93
args = sys.argv[1:] # ignore the first arg as it is the .py file
robot_id = args[0]
rospy.init_node('map_node_' + robot_id)
rss_map_with_position_pub = rospy.Publisher(robot_id + "/rss_map_with_position", Image, queue_size=2)
args = sys.argv[2:]
args = tuple(map(float, args))
bridge = CvBridge()

scene = mi.load_file("../scenes/tunnel.xml")

# Initialize the MapTracer
tracer = MapTracer(scene,
    fc=2.4e9,                             # Carrier frequency [Hz]
    tx_pattern='hw_dipole',               # Transmit antenna pattern, 'iso' 'dipole', 'hw_dipole', or 'tr38901'
    tx_slant_angle=0.0,                   # Slant angle for the linearly polarized antenna [rad].
                                          # Zero means vertical polarization
    mp_center = np.array([0., 0., 0.]),   # Position of the center of the measurement plane
    mp_orientation = np.array([0.,0.,0.]),# Orientation of the measurement plane [alpha, beta, gamma].
                                          # [0,0,0] means the normal to the map is z
    mp_size = np.array([800.,800.]),      # Size of the measurement plane
    mp_cell_size = np.array([1,1]),       # Size of cells of the measurement plane
    num_samples = int(1e7),               # Number of rays initially shot from the transmitter
    max_depth = 10)                       # Maximum number of bounces

tx_position=np.array([args[0], args[1], 0.0]) + offset
tx_orientation=np.array([np.pi, 0., 0.])
pm, rdsm, mdam, mddm=tracer(tx_position, tx_orientation)
pm = pm.numpy()
# Convert to dB 
pm_db = np.where(pm == 0., np.nan, 10. * np.log10(pm + 1e-12))
x_start, x_end = 350, 700
y_start, y_end = 50, 450
cropped_rss_map = pm_db[x_start:x_end, y_start:y_end]

rss_map_with_position = bridge.cv2_to_imgmsg(cropped_rss_map.astype(np.float32), encoding="32FC1")
rss_map_with_position_pub.publish(rss_map_with_position)
# print("publish rss map for " + robot_id)

rss_map_with_position_pub.unregister()
del rss_map_with_position_pub

# rospy.loginfo("RSS map Published")