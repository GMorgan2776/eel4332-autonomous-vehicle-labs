"""Starter code for the EEL 4332 kinematic bicycle model."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class BicycleState:
    """Planar bicycle-model pose; x and y are in m and yaw is in rad."""

    x: float
    y: float
    yaw: float


def wheel_speed_to_twist(
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
) -> tuple[float, float]:
    """Return body-forward speed and yaw rate for the bicycle model.

    Parameters are SI units:
      wheel_speed: equivalent driven-wheel angular velocity in rad/s
      wheel_radius: effective driven-wheel radius in m
      steering: equivalent front-wheel steering angle in rad
      wheelbase: distance between equivalent front and rear axles in m

    Returns:
      linear_speed: body-forward speed in m/s
      yaw_rate: vehicle yaw rate in rad/s

    TODO:
      1. Convert driven-wheel angular velocity to body-forward speed using
         ideal rolling without slip.
      2. Use the bicycle-model steering geometry to compute vehicle yaw rate.
      3. Return body-forward speed and vehicle yaw rate.

    Hints:
      - Start with the tangential speed at the driven wheel's rim.
      - Zero steering must give zero yaw rate.
      - For fixed speed and wheelbase, increasing steering magnitude should
        increase yaw-rate magnitude.
    """
    linear_speed = wheel_radius * wheel_speed;
    yaw_rate = (linear_speed / wheelbase) * np.tan(steering);

    return linear_speed, yaw_rate;

    raise NotImplementedError("TODO: implement wheel_speed_to_twist")


def step_bicycle(
    state: BicycleState,
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
    dt: float,
) -> BicycleState:
    """Advance the planar kinematic bicycle model by one time step.

    Parameters are SI units:
      state: current planar pose; x and y in m, yaw in rad
      wheel_speed: equivalent driven-wheel angular velocity in rad/s
      wheel_radius: effective driven-wheel radius in m
      steering: front-wheel steering angle in rad
      wheelbase: distance between equivalent front and rear axles in m
      dt: integration time step in s

    Returns:
      BicycleState: new pose after one time step; x and y in m, yaw in rad

    TODO:
      1. Call wheel_speed_to_twist.
      2. Express body-forward speed in the world frame using state.yaw.
      3. Integrate one step.
      4. Return the new state.

    Hint: use the current yaw, not the newly updated yaw, when computing this
    explicit Euler step's world-frame position rates.
    """
    linear_speed, yaw_rate = wheel_speed_to_twist(wheel_speed, wheel_radius, steering, wheelbase);

    speed_x = linear_speed * np.cos(state.yaw);
    speed_y = linear_speed * np.sin(state.yaw);
    speed_yaw = (linear_speed / wheelbase) * np.tan(steering);

    step_x = state.x + speed_x * dt;
    step_y = state.y + speed_y * dt;
    step_yaw = state.yaw + speed_yaw * dt;

    return BicycleState(step_x, step_y, step_yaw);

    raise NotImplementedError("TODO: implement step_bicycle")


def simulate(
    initial_state: BicycleState,
    wheel_speed: float,
    wheel_radius: float,
    steering: float,
    wheelbase: float,
    dt: float,
    duration: float,
) -> np.ndarray:
    """Return an N x 3 trajectory for a constant-input experiment.

    Parameters are SI units:
      initial_state: pose at time zero; x and y in m, yaw in rad
      wheel_speed: constant equivalent driven-wheel angular velocity in rad/s
      wheel_radius: effective driven-wheel radius in m
      steering: constant front-wheel steering angle in rad
      wheelbase: distance between equivalent front and rear axles in m
      dt: fixed integration time step in s
      duration: requested simulation duration in s

    Returns:
      np.ndarray: trajectory with one pose per row and columns [x, y, yaw];
      x and y are in m and yaw is in rad

    TODO: repeatedly call step_bicycle and store the trajectory.

    Hint: store initial_state first, then repeatedly advance from the most
    recently returned BicycleState until all fixed time steps are complete.
    """
    trajectory = np.zeros((int(duration / dt) + 1, 3));
    trajectory[0] = [initial_state.x, initial_state.y, initial_state.yaw];

    current_state = initial_state;

    for i in range(1, trajectory.shape[0]):
        current_state = step_bicycle(current_state, wheel_speed, wheel_radius, steering, wheelbase, dt)
        trajectory[i] = [current_state.x, current_state.y, current_state.yaw];

    return trajectory;
    raise NotImplementedError("TODO: implement simulate")
