import math

from src.kinematics import forward_kinematics
from src.motion import trajectory_to_angles


def test_trajectory_to_angles():
    trajectory = [
        (1.0, 1.0),
        (0.0, 2.0),
    ]

    angles = trajectory_to_angles(trajectory)

    assert len(angles) == len(trajectory)

    for (theta1, theta2), (x, y) in zip(angles, trajectory):
        calculated_position = forward_kinematics(theta1, theta2)

        assert math.isclose(
            calculated_position[0],
            x,
            abs_tol=1e-9,
        )

        assert math.isclose(
            calculated_position[1],
            y,
            abs_tol=1e-9,
        )