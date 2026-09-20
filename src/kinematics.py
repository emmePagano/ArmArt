import math


def joint_positions(
    theta1: float,
    theta2: float,
    l1: float = 1.0,
    l2: float = 1.0,
) -> tuple[tuple[float, float], tuple[float, float]]:
    """
    Calculate the positions of the two joints.

    Angles are expressed in radians.
    """
    x1 = l1 * math.cos(theta1)
    y1 = l1 * math.sin(theta1)

    x2 = x1 + l2 * math.cos(theta1 + theta2)
    y2 = y1 + l2 * math.sin(theta1 + theta2)

    return (x1, y1), (x2, y2)


def forward_kinematics(
    theta1: float,
    theta2: float,
    l1: float = 1.0,
    l2: float = 1.0,
) -> tuple[float, float]:
    """
    Calculate the end-effector position of a 2-link robotic arm.

    Angles are expressed in radians.
    """
    _, end_effector = joint_positions(theta1, theta2, l1, l2)

    return end_effector