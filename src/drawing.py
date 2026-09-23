from dataclasses import dataclass

from src.trajectory import line_trajectory


@dataclass
class DrawingOperation:
    """Represent a drawing or travel operation."""

    operation_type: str
    points: list[tuple[float, float]]


def create_drawing() -> list[DrawingOperation]:
    """Create a drawing composed of multiple operations."""

    first_stroke = line_trajectory(
        start=(0.2, 0.2),
        end=(0.8, 0.2),
        steps=20,
    )

    second_stroke = line_trajectory(
        start=(0.5, 0.2),
        end=(0.5, 0.8),
        steps=20,
    )

    travel = line_trajectory(
        start=(0.8, 0.2),
        end=(0.5, 0.2),
        steps=10,
    )

    return [
        DrawingOperation("DRAW", first_stroke),
        DrawingOperation("TRAVEL", travel),
        DrawingOperation("DRAW", second_stroke),
    ]