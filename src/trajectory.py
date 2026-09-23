import math


def line_trajectory(
    start: tuple[float, float],
    end: tuple[float, float],
    steps: int = 20,
) -> list[tuple[float, float]]:
    """Generate points along a straight-line trajectory."""

    if steps < 2:
        raise ValueError("steps must be at least 2")

    x_start, y_start = start
    x_end, y_end = end

    trajectory = []

    for i in range(steps):
        t = i / (steps - 1)

        x = x_start + t * (x_end - x_start)
        y = y_start + t * (y_end - y_start)

        trajectory.append((x, y))

    return trajectory



def circle_trajectory(
    center: tuple[float, float],
    radius: float,
    steps: int = 100,
) -> list[tuple[float, float]]:
    """Generate points along a circular trajectory."""

    if radius <= 0:
        raise ValueError("radius must be positive")

    if steps < 3:
        raise ValueError("steps must be at least 3")

    center_x, center_y = center

    trajectory = []

    for i in range(steps):
        angle = 2 * math.pi * i / steps

        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        trajectory.append((x, y))

    return trajectory