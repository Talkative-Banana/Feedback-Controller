[Specs]
Ubuntu 24.04
ros2 jazzy gz harmonic
colcon for build

# How to install
[*] ros2

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null	

sudo apt install ros-jazzy-desktop

[*] Gz

sudo apt-get install curl
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

sudo apt-get update

sudo apt-get install gz-harmonic

[*] Get TurtleBot4

Need to build from src (I am providing already built files in the zip 'Turtlebot')

[*] Setup

1) I have updated the maze world (removed all the walls of maze) and build the package again ('Turtlebot')
2) Our Controller lies in separate package (independent package ('Feedback_Controller'))

[*] How to run
1) Open 3 terminals
2) Terminal1$ cmd Turtlebot
   Terminal1$ source ./install/setup.bash
   Terminal1$ ros2 launch turtlebot4_gz_bringup turtlebot4_gz.launch.py world:=maze
   

   wait for it to boot and undock the bot from gui

   Terminal2$ cmd Feedback_Controller
   Terminal2$ ros2 run fc controller

   Terminal3$ ros2 topic info /cmd_vel --verbose
   Terminal3$ ros2 lifecycle set cmd_vel_bridge shutdown

You will have a running Turtlebot :)
