# ROS2 Humble TurtleSim Project

This project demonstrates a simple ROS2 application using the TurtleSim package. In this project, you control a turtle using a joystick connected to an Arduino Uno. The joystick inputs are read using `pyserial` and sent to ROS2 to control the turtle's movement.

## Table of Contents
- [What is this Project](#what-is-this-project)
- [What I Learnt from this Project](#what-i-learnt-from-this-project)
- [Concepts Used in this Project](#concepts-used-in-this-project)
- [How to Clone and Use this Repo](#how-to-clone-and-use-this-repo)

## What is this Project
This project is a demonstration of using ROS2 (Robot Operating System 2) with the TurtleSim package to create a simple simulation where a turtle is controlled by a joystick connected to an Arduino Uno. The project helps to understand the basics of ROS2 nodes, topics, and using `pyserial` for serial communication.

## What I Learnt from this Project
Through this project, I have learnt:
- How to set up and configure a ROS2 workspace.
- The basics of creating and running ROS2 nodes using Python.
- How to use ROS2 topics to publish and subscribe to messages.
- Implementing teleoperation using joystick inputs.
- Using `pyserial` to read data from the Arduino.
- Integrating Arduino with ROS2 for controlling simulations.

## Concepts Used in this Project
- **ROS2 Nodes**: Independent processes that perform computation.
- **ROS2 Topics**: Channels for nodes to communicate with each other by publishing and subscribing to messages.
- **TurtleSim**: A ROS2 package used to simulate a turtle's movement in a 2D space.
- **Teleoperation**: Controlling the turtle using joystick inputs.
- **Serial Communication**: Using `pyserial` to read data from the Arduino.

## How to Clone and Use this Repo

### Set up your ROS2 workspace

1. Create a workspace:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone git@github.com:AshishNith/Turtle_follow.git
    cd ~/ros2_ws
    colcon build
    source ~/ros2_ws/install/setup.bash
    ```

### How to run this

1. Launch the TurtleSim node:
    ```bash
    ros2 run turtlesim turtlesim_node
    ```
2. Run the joystick control node:
    ```bash
    ros2 run turtle_joystick joystick_control
    ```

Ensure the Arduino is connected to your computer and is running the appropriate sketch for reading joystick inputs and sending them via serial.

## Conclusion
This project provides a basic understanding of integrating hardware inputs with ROS2 to control simulations. It covers setting up a ROS2 workspace, writing and running ROS2 nodes, and using serial communication with Arduino.
