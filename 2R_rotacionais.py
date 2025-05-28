import roboticstoolbox as rtb
from spatialmath import SE3
import numpy as np

# Define the 2R robot using DH parameters: [theta, d, a, alpha]
L1 = rtb.DHLink(theta=0, d=0, a=100, alpha=0, mdh=0)  # Link 1 at origin
L2 = rtb.DHLink(theta=0, d=0, a=50, alpha=0, mdh=0)   # Link 2 

# Create the robot with base at the origin
robot = rtb.DHRobot([L1, L2], name='2R Planar Robot', base=SE3())

# Print robot details
print(robot)

# Example: Forward kinematics for joint angles [30°, 90°]
q = np.deg2rad([30, 90])
T = robot.fkine(q)
print("End-effector pose:\n", T)

# Plot the robot's position for the given joint angles
robot.teach(q, block=True)
