#!/usr/bin/env python3
 
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
 
class SetWayPoint(Node):
 
    def __init__(self):
        super().__init__('set_way_point')
 
        self.pose = None
 
        # waypoint
        self.waypoint = (7.0, 7.0)
 
        # constante
        self.Kp = 2.0
 
        # subscriber
        self.subscriber = self.create_subscription(
            Pose,
            'pose',
            self.pose_callback,
            10
        )
 
        # publisher
        self.publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )
 
    def pose_callback(self, msg):
        self.pose = msg
 
        # position actuelle
        xA = msg.x
        yA = msg.y
 
        # waypoint
        xB = self.waypoint[0]
        yB = self.waypoint[1]
 
        # angle désiré
        theta_desired = math.atan2(yB - yA, xB - xA)
 
        # angle actuel
        theta = msg.theta
 
        # erreur
        error = math.atan(math.tan((theta_desired - theta) / 2))
 
        # commande
        u = self.Kp * error
 
        # message cmd_vel
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = u
 
        self.publisher.publish(cmd)
 
        # affichage
        self.get_logger().info(f"Erreur: {error:.2f}, Commande: {u:.2f}")
 
 
def main(args=None):
    rclpy.init(args=args)
    node = SetWayPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == '__main__':
    main()
 
