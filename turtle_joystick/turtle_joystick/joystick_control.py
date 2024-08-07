#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import serial

class JoystickControl(Node):
    def __init__(self):
        super().__init__('joystick_control')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        if self.serial_port.in_waiting > 0:
            data = self.serial_port.readline().decode('utf-8').strip()
            if data.startswith("X:") and ",Y:" in data:
                x_str, y_str = data.split(",Y:")
                x_val = int(x_str.split(":")[1])
                y_val = int(y_str)

                twist = Twist()
                twist.linear.x = (y_val - 512) / 512.0
                twist.angular.z = (x_val - 512) / 512.0
                self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = JoystickControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
