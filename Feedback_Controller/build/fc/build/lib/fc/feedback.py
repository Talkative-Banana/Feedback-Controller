#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry
from math import atan2, sqrt, sin, cos

class Unicycle_Controller(Node):
    def __init__(self):
        super().__init__('unicycle_controller')

        # Initialize publisher
        self.pub = self.create_publisher(TwistStamped, '/cmd_vel', 10)
        self.odom_sum = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        self.timer = self.create_timer(0.1, self.control_loop)

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Waypoints
        self.waypoints = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Current index
        self.cidx = 0;
        self.get_logger().info("GUI Controller node initialized") 

    def odom_callback(self, msg):
        # Update the robot's position and orientation
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.get_logger().info(f"Cords received {self.x} {self.y}\n")
        # Extract orientation (quaternion to Euler)
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y ** 2 + q.z ** 2)
        self.theta = atan2(siny_cosp, cosy_cosp)
        return;

    def control_loop(self):
        target_x, target_y = self.waypoints[self.cidx]
    
        # Compute distance and target angle
        distance = sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)
        target_angle = atan2(target_y - self.y, target_x - self.x)

        # Check if the waypoint is reached
        if distance < 0.1:
            self.cidx = (self.cidx + 1) % 4

        # Compute control commands
        twist = TwistStamped()
        twist.header.stamp = self.get_clock().now().to_msg()  # Add timestamp
        twist.twist.linear.x = 2.0 if distance > 0.1 else 0.0  # Linear velocity
        twist.twist.angular.z = 2.0 * atan2(sin(target_angle - self.theta), cos(target_angle - self.theta))  # Angular velocity

        # Publish velocity commands
        self.pub.publish(twist)
        return

def main(args=None):
    rclpy.init()
    gui_controller = Unicycle_Controller()

    try:
        rclpy.spin(gui_controller)
    except KeyboardInterrupt:
        gui_controller.get_logger().info("Shutting down")
    finally:
        gui_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
   main()
