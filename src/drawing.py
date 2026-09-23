from src.trajectory import line_trajectory


def create_drawing() -> list[list[tuple[float, float]]]:
    """Create a drawing composed of multiple strokes."""

    strokes = [
        line_trajectory(
            start=(0.2, 0.2),
            end=(0.8, 0.2),
            steps=20,
        ),
        line_trajectory(
            start=(0.5, 0.2),
            end=(0.5, 0.8),
            steps=20,
        ),
    ]

    return strokes