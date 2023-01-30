#!/usr/bin/env python3
import rclpy  # Python Client Library for ROS 2
from rclpy.node import Node  # Handles the creation of nodes
from sensor_msgs.msg import Image  # Image is the message type
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge  # ROS2 package to convert between ROS and OpenCV Images
import cv2  # Python OpenCV library
import numpy as np

cv_image = np.zeros((512,700,3), np.uint8)
msg = Twist()

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.i = 0
        self.direction = 100

    def pub_direction(self):
        if self.direction == 1:
            msg.linear.x = 2.0
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = 2.0
            self.publisher_.publish(msg)

        elif self.direction == 2:
            msg.linear.x = 2.0
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x = 0.0
            msg.angular.y = 0.0
            msg.angular.z = -2.0
            self.publisher_.publish(msg)

        print(self.i)
        self.i += 1

    def image_capture(self):
        # reading the image
        cv_image = np.zeros((512, 700, 3), np.uint8)

        # displaying the image
        cv2.imshow('image', cv_image)

        # setting mouse handler for the image
        # and calling the click_event() function
        cv2.setMouseCallback('image', self.click_event)

        # wait for a key to be pressed to exit
        cv2.waitKey(0)

        # close the window
        cv2.destroyAllWindows()

    # function to display the coordinates of
    # of the points clicked on the image
    def click_event(self, event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            if x <= 350:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(cv_image, str(x) + ',' +
                            str(y), (x, y), font,
                            1, (255, 0, 0), 2)
                self.direction = 1
                print('LEFT')
            else:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(cv_image, str(x) + ',' +
                            str(y), (x, y), font,
                            1, (0, 255, 0), 2)
                self.direction = 2
                print('RIGHT')

            cv2.imshow('image', cv_image)
            self.pub_direction()

# driver function
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    minimal_publisher.image_capture()

    rclpy.spin(minimal_publisher)
    rclpy.shutdown()


if __name__ == '__main__':
    main()