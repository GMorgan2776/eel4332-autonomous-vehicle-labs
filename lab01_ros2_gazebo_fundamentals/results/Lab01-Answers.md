# Lab 1 Answers

## Recorded Measurements

1. Measured `/chatter` publication rate:
Average Rate: 1.000

2. Measured `/practice/count` rate with `rate_hz:=5.0`: 
Average Rate: 5.000

3. Measured `/practice/count` rate with `rate_hz:=2.0`:
Average Rate: 2.000

4. Original red-box pose: 
X = 0.00
Y = 0.00
Z = 1.50
Roll = 0.00
Pitch = 0.00
Yaw = 0.00

5. Modified red-box pose:
X = -1.00
Y = 0.00
Z = 1.50
Roll = 0.00
Pitch = 0.00
Yaw = 0.00

6. Observation of simulation time while Gazebo was playing and paused:

While playing, the "real" and "sim" timers move as you'd expect, increasing as time flows. It should be noted that the "real" timer is slightly faster than the "sim" timer, and the "system" timer increments normally.
While paused, the "system" time advances, but the "real" and "sim" time do not.
When reset, the "sim" and "real" timers hold no value, the "system" time continues to increment.

## Engineering Questions

1. In your own words, distinguish a ROS topic, service, action, and parameter. Give one appropriate use for each.

An ROS Topic is like a data cable, it allows for data to be streamed between nodes. We use Topics to allow for sensor readings on robots.

ROS Services are like simple commands you can issue to ROS Nodes. Services are typically used for reading from and writing to Node parameters. On Robots, Services are useful for reseting parameters, which can simplify loops if the Robot returns to the starting position.

ROS Actions are long, muti-step commands you can issue to ROS Nodes. We use these for complex actions such as rotation or goal/point navigation.

ROS Parameters are very simple configuration values for Nodes that are controlled BY the Node itself. These are things such as colors, names, and the update rate of the Node. We can use Parameters to change the color of lights on a Robot.

2. Why must a newly built workspace be sourced before `ros2 run` or `ros2 launch` can find its packages?

Because ROS2 cannot scan your entire computer to find packages, and because each workspace is located in its own unique filesystem path, it needs package paths that are defined in the setup script for the workspace you intend to work in.

3. What evidence showed that Gazebo Transport and the ROS graph are separate communication systems?

The fact that you need to create a bridge between the two systems in order for ROS to read Gazebo values.

4. What did the `/clock` bridge do? What happened on the ROS side when the bridge stopped?

The Bridge enabled ROS to read te clock value of the simulation as long as the bridge was up. When the bridge was stopped, ROS could no longer read the clock value, giving the error "Unknown topic '/clock'"

5. Explain how the measured message rates changed when the launch argument changed.

Because the launch argument controlled the Hz rate of messages being sent, when you change that launch argument, the measured rate changes to be about that Hz value. 
