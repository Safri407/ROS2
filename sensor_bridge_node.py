#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Example message type

class SensorBridge(Node):
    def __init__(self):
        super().__init__('sensor_bridge_node')
        self.publisher_ = self.create_publisher(String, 'sensor_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = String()
        msg.data = "Hello from sensor bridge"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = SensorBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

