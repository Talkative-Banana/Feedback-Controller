# Uni-Cycle Robot Feedback Controller

# Objective
The goal is to design a feedback controller that ensures the robot visits the four specified coordinates periodically while maintaining a constant linear velocity of 2 units at these positions.

## 1. Install ROS 2 Jazzy
```bash
# Set up the ROS 2 repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/rosarchive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install the ROS 2 Jazzy Desktop package
sudo apt install ros-jazzy-desktop
```

## 2. Install Gazebo Harmonic
```bash
# Install curl if not already installed
sudo apt-get install curl

# Download and install the Gazebo GPG key
sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

# Add the Gazebo repository to your system
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

# Update the apt repository
sudo apt-get update

# Install Gazebo Harmonic
sudo apt-get install gz-harmonic
```

## 3. Clone and Build TurtleBot4 from Source (Optional)
```bash
# If you have pre-built TurtleBot files, you can skip this step. To build from source:

# Clone the TurtleBot4 repository
cd ~/ros2_ws/src
git clone <TURTLEBOT4_REPO_URL>

# Build the workspace using colcon
cd ~/ros2_ws
colcon build

# Source the workspace setup file
source install/setup.bash
```

## 4. Install the Feedback Controller
```bash
# The feedback controller package is independent and needs to be built separately.

# Clone the Feedback_Controller package into your workspace
cd ~/ros2_ws/src
git clone <FEEDBACK_CONTROLLER_REPO_URL>

# Build the workspace
cd ~/ros2_ws
colcon build

# Source the workspace setup file
source install/setup.bash
```

## 5. Setup Maze World
```bash
# The maze world has been updated to remove all walls. 
# Make sure the Turtlebot package has been built after these modifications.
# Rebuild the package if needed.

cd ~/ros2_ws
colcon build
source install/setup.bash
```

## 6. Run the System

```bash
# To launch the TurtleBot4 and control it, you will need to use three terminals.

# Terminal 1: Launch TurtleBot4 in Gazebo
source ./install/setup.bash
ros2 launch turtlebot4_gz_bringup turtlebot4_gz.launch.py world:=maze
# Wait for the robot to boot and undock from the GUI.

# Terminal 2: Run the Feedback Controller
ros2 run fc controller

# Terminal 3: Monitor the /cmd_vel Topic
ros2 topic info /cmd_vel --verbose
```

### Shutdown the cmd_vel Bridge
ros2 lifecycle set cmd_vel_bridge shutdown
