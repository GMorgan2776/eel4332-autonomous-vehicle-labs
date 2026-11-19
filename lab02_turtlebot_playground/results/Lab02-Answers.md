# Lab 2 Answers — TurtleBot Playground

## Driving observations

Describe what you observed during forward, reverse, curved, and in-place motion.

Forward motion caused the robot to move forward at 0.15 speed along its X-axis
Reverse motion caused the robot to move backward at 0.15 speed, equating to -0.15 speed along its X-axis
Curved motion caused a 0.15 X-axis speed (-0.15 if reversing) and a 0.80 angular speed along its Z-Axis. (+0.8 along Z-rotation for left turning, -0.8 along Z-rotation for right turning)
When turning in place, it functions exactly the same as the curved motion but without the X-Axis movement, so there's only +/- 0.8 Z-Rotation motion depending on the direction of rotation

## Challenge screenshot

Insert or link one screenshot showing TurtleBot during or after a driving challenge.

This is linked on canvas, I'm not sure how to embed images in a file like this in Visual Studio Code:

C:\Users\thein\Downloads\Lab02-SlalomChallengeResults.png
lab02_turtlebot_playground/results/Lab02-SlalomChallengeResults.png

I don't know if that will actually embed, just check the Canvas submission.

## ROS signal preview

### Forward `/cmd_vel`

Record or paste one representative message.

thein@Gabriel-VICTUS:~/courses/eel4332-autonomous-vehicle-labs$ source /opt/ros/jazzy/setup.bash
ros2 topic echo /cmd_vel
linear:
  x: 0.15
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
---
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
---

### Turning `/cmd_vel`

Record or paste one representative message.

thein@Gabriel-VICTUS:~/courses/eel4332-autonomous-vehicle-labs$ source /opt/ros/jazzy/setup.bashsh
ros2 topic echo /cmd_vel
linear:
  x: 0.15
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.8
---
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
---
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: -0.8
---
linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
---

### `/odom` change

Record the before-and-after values of one position or orientation field around the direct terminal command and identify what changed.

BEFORE:

thein@Gabriel-VICTUS:~/courses/eel4332-autonomous-vehicle-labs$ ros2 topic echo /odom --oncece
header:
  stamp:
    sec: 391
    nanosec: 716000000
  frame_id: odom
child_frame_id: base_footprint
pose:
  pose:
    position:
      x: 0.36441718332543427
      y: -0.004826404040726778
      z: 0.0
    orientation:
      x: 0.0
      y: -0.0
      z: -0.00019934916332144513
      w: -0.9999999801299554
  covariance:
  - 0.0
  - 0.0

...

AFTER:

thein@Gabriel-VICTUS:~/courses/eel4332-autonomous-vehicle-labs$ ros2 topic echo /odom --once
header:
  stamp:
    sec: 454
    nanosec: 824000000
  frame_id: odom
child_frame_id: base_footprint
pose:
  pose:
    position:
      x: 0.6416171612965763
      y: -0.004715884866622709
      z: 0.0
    orientation:
      x: 0.0
      y: -0.0
      z: -0.00019934916347998498
      w: -0.9999999801299553
  covariance:
  - 0.0
  - 0.0

  ...

  The X and Y positions of the robot (relative to the workspace, not to itself) changed. The X-Position increased by ~0.3 and the Y-Position increased by ~0.0001 the change in Y-Position is because the robot was at a slight angle to start with, so when it moved forward it also moved a bit along the Y-Axis of the workspace.

## Engineering questions

Answer Questions 1–4 from the README using observations from your own simulation session.

1. Which linear.x and angular.z values changed for forward motion, turning, and stopping, and how did the keyboard node and direct terminal command publish the same kind of command?

during forward motion, linear.x increased to 0.15, during reverse motion it decreased to -0.15
during turning, angular.z increased to 0.80 when turning left, decreased to -0.80 when turning right.
during curving, linear.x changed to +/- 0.15 depending on forward/backward instruction, and angular.z changed to +/- 0.80 depending on left/right instruction.
during stopping, angular.z and linear.x both go to 0.00

The keyboard node took in keyboard inputs and processed them into motion instructions, which required some delays for processing. The terminal command instantly sends the same kind of instructions without delays, but requires you to plan out the desired path and cannot be adjusted in real time through the keyboard.

2. Which position or orientation fields changed in /odom, and why is odometry called an estimate?

The only position and orientation fields that changed in /odom were those of the realtive position of the robot in the workspace. Odometry is called an estimate because it etimates the position of the robot by adding together all of the small, measured changes made over a period of time rather than directly reading the absolute position from the program.

3. Why is a /cmd_vel velocity command alone insufficient to make the robot reach a specified destination?

The /cmd_vel command is insufficient at this alone because it is a topic/communication channel, not a controller or destination. It can only tell the robot to move forward or backward at any given instant, it cannot tell it to move to a specific location on its own.

4. In this playground, which observe–decide–command tasks did you perform that autonomous software must perform later?

Dodging Obstacles, this required observing where the robot was in relation to a pillar in order to decide when it should be commanded to start curving around it. 