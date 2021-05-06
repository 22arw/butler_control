#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"

bool buttonPressed = false;
bool running = true;

void velCallback(const std_msgs::String::)
{
  if msg == "stop"
  {
    ROS_INFO("stop")
    buttonPressed = false;
  }

  if msg == "start"
  {
    ROS_INFO("start")
    buttonPressed = true;
  }
}



int main(int argc, char **argv)
{
  ros::Publisher cmd_vel_pub <advertise<geometry_msgs::Twist>("cmd_vel", 1, true);

  geometry_msgs::Twist cmd_vel_msg;

  cmd_vel_msg.linear.x = 0
  cmd_vel_msg.linear.y = 0
  cmd_vel_msg.linear.z = 0
  cmd_vel_msg.angular.z = 0
  cmd_vel_msg.angular.y = 0
  cmd_vel_msg.angular.x = 0

  ros::init(argc, argv  , "listener");

  ros::NodeHandle n;

  ros::subscriber sub = n.subscribe("velShutDown", 1000, velCallback);

  while (running)
  {
    while (!buttonPressed)
    {
      cmd_vel_pub.publish(cmd_vel_msg);
    }
  }
  return 0;
}
