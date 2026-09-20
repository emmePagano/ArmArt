import math


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
    x = (
        l1 * math.cos(theta1)
        + l2 * math.cos(theta1 + theta2)
    )

    y = (
        l1 * math.sin(theta1)
        + l2 * math.sin(theta1 + theta2)
    )

    return x, y