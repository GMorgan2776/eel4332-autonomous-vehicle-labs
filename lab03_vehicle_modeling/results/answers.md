# Lab 3 Answers

## Part 1 predictions

Record the predicted motion and signs of body-forward speed and vehicle yaw rate for each wheel-angular-velocity case.

See Canvas Submission for:

/home/thein/courses/eel4332-autonomous-vehicle-labs/lab03_vehicle_modeling/results/Lab03-PracticeProblemsPart1.png

lab03_vehicle_modeling/results/Lab03-PracticeProblemsPart1.png

## Differential-drive validation

Summarize the final pose of each special case and explain any disagreement with your hand prediction.

All of the final poses for each special case match my hand prediction.
Equal Positive - +X 0YAW
Left Wheel Stationary - +X +YAW
Equal and Opposite: 0X +YAW
Slight Mismatch: +X -YAW

## Student motion-design challenge

Select one target. Before running the program, record the wheel-speed relationship or calculation you used. After running it, record the chosen values and resulting final pose.

| Motion target | Predicted wheel-speed relationship or calculation | Chosen $\omega_L$ [rad/s] | Chosen $\omega_R$ [rad/s] | Final $(x,y,\theta)$ | Target met? |
|---|---|---:|---:|---|---|
| selected target: | See Canvas Submission for: lab03_vehicle_modeling/results/Lab03-StudentModelCalculations.png | -2.99 | -2.99 | (-0.792, 0, 0) | Yes |

## TurtleBot visual checkpoint

Insert one screenshot showing TurtleBot during a commanded motion case and identify whether it shows straight motion, curved motion, or in-place rotation.

Check Canvas Submission for: 
lab03_vehicle_modeling/results/Lab03-TurtlebotAllMovementCommandsResult.png

This is a picture taken after ALL movement commands were executed.

Record the `pose.pose.position.x` and `.y` values from `/odom` before and after the straight command. Briefly explain how this change relates to the pose integration in `differential_drive.py`.

BEFORE:
X = 2.371907
Y = 3.322722

AFTER:
X = 0.37935
Y = 1.12708

Odometry is an estimate created by the sum of all trajectory pings, this relates to what I created in the Python script because there, we created the trajectory array by which Odometry calculations are made from step-by-step.

## Bicycle-model observations

Record the body-forward speed and yaw rate produced by `wheel_speed_to_twist` for each case. Explain the effects of zero steering and increasing steering magnitude.

See Canvas Submission for: 

lab03_vehicle_modeling/results/Lab03-BicycleTests.png

The impact of zero steering, as seen in test 01, is a Yaw Rate of Zero.
As steering magnitude increases, as seen between test 02 and 03, the Yaw Rate increases.

This aligns with how yaw rate is calculated for both Bicycle Robots and Differential-Drive Robots, as when you turn, you increase your turning/yaw rate. Granted, a Bicycle Robot would be incapable of turning in place.

## Model comparison

Compare the inputs, motion capabilities, and limitations of ideal differential drive and the kinematic bicycle model.

Differential-Drive Robots and Bicycle Robots both share similar inputs, in fact, they share pretty much exactly the same inputs relative to each other. However, where Differential-Drive Robots differ from Bicycle Robots comes in the ability to rotate while stationary. Differential Drive Robots can perform more articulated motion because of this, and can navigate rat mazes where Bicycle Models cannot. 

Ideal DD Robots have limitations in the fact that they cannot handle uphill movements as gracefully as Bicycle Robots, due to the reliance on a forward-facing drive ball. Kinematic Bicycle Robots, as explained previously, cannot turn in place

## Engineering questions

Answer Questions 1–6 from the README. Use equations, units, plots, or table values where they support your explanation.

1. Why is integrating wheel-derived velocity called dead reckoning?

Because much like the historical nautical navigational tactic, "Deductive (Ded.) Reckoning" where navigators would estimate current positions based on known positions and speed from previously, integrating wheel-derived velocity provides you an estimated future position based on current and past values.

2. Which differential wheel-angular-velocity combinations produce straight motion, curved motion, and an in-place turn?

Straight Motion: wL = wR = w
Curved Motion: wL > wR for Right Curve, wL < wR for Left Curve
In-Place Turning: wL = 0 and wR > 0 for Left Turn, wL > 0 and wR = 0 for Right Turn

3. Why can a small wheel-radius or wheel-angular-velocity mismatch create a large position error after a long drive?

An angular velocity mismatch can cause large position errors because the mismatch causes the vehicle to slightly curve over time.
Small wheel radii can cause position errors over time because small changes in the wheel's rotation angle can cause the same kind of subtle drifting as mismatched angular velocities.

4. Why is /odom an estimate rather than ground truth?

Because Odometry is the summation of all previous positions and speeds, A.K.A the Dead Reckoning mentioned previously. This makes it prone to long-term errors caused by slight changes in attributes. 

5. Why can the bicycle model not represent an in-place turn?

The Bicycle Model outlined in this lab is incapable of in-place turning because the angular velocity relies on the forward/backward speed of the Robot. Additionally, the "build" of the Bicycle Model is incapable of in-place turning because the hind wheels cannot turn, only the front ones.

6. How do wheelbase and steering angle affect bicycle-model turning radius?

The length of the Wheelbase is directly proportional to the size of the turning radius, as Wheelbase increases/decreases, turning radius increases/decreases. This is because as the Wheelbase increases, more space is needed for the vehicle to make a turn.

Steering Angle in inversely proportional to the size of the turning radius, as Steering Angle increases/decreases, turning radius decreases/increases. This is because the Steering Angle is in the denominator for the equation for Turning Radius: R = L/tan(sigma)
More practically, it's because the increased steering angle shortens the distance between the endpoint of the turning radius and the centerpoint of the distance between the two front wheels. 


