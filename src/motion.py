from src.kinematics import inverse_kinematics


def trajectory_to_angles(
    trajectory: list[tuple[float, float]],
    l1: float = 1.0,
    l2: float = 1.0,
) -> list[tuple[float, float]]:
    """Convert Cartesian trajectory points into joint angles."""

    angles = []

    for x, y in trajectory:
        theta1, theta2 = inverse_kinematics(
            x,
            y,
            l1,
            l2,
        )

        angles.append((theta1, theta2))

    return angles