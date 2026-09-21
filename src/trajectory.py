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