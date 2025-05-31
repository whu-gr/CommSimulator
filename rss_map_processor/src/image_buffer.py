
import rospy
from sensor_msgs.msg import Image

class RssMapRepublisher:
    def __init__(self):
        rospy.init_node('rss_map_republisher')
        robot_id = rospy.get_param('~robot_id', 'wheeled0')

        sub_topic = "/sensor_coverage_planner/" + str(robot_id) + "/rss_map_with_position"
        pub_topic = "/sensor_coverage_planner/" + str(robot_id) + "/rss_map_with_position_repub"

        self.subscriber = rospy.Subscriber(sub_topic, Image, self.callback)
        self.publisher = rospy.Publisher(pub_topic, Image, queue_size=5)
        self.rate = rospy.Rate(10)  # 10Hz

        self.latest_msg = None

    def callback(self, msg):
        self.latest_msg = msg

    def publish_loop(self):
        while not rospy.is_shutdown():
            if self.latest_msg is not None:
                if self.latest_msg.height > 0 and self.latest_msg.width > 0:
                    self.publisher.publish(self.latest_msg)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        republisher = RssMapRepublisher()
        republisher.publish_loop()
    except rospy.ROSInterruptException:
        pass
