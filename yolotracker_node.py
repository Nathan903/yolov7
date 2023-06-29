import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
from detect_or_track import *

class DetectionNode(Node):
    def __init__(self):
        super().__init__('detection_node')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            'camera',
            self.image_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def image_callback(self, msg):
        image_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        detect(image_frame)

def main(args=None):
    rclpy.init(args=args)
    detection_node = DetectionNode()
    rclpy.spin(detection_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
