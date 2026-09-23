import math

import pytest

from src.trajectory import circle_trajectory, line_trajectory


def test_line_trajectory():
    trajectory = line_trajectory(
        (0.0, 0.0),
        (2.0, 2.0),
        steps=3,
    )

    assert trajectory == [
        (0.0, 0.0),
        (1.0, 1.0),
        (2.0, 2.0),
    ]


def test_line_trajectory_requires_two_steps():
    with pytest.raises(ValueError):
        line_trajectory(
            (0.0, 0.0),
            (1.0, 1.0),
            steps=1,
        )





def test_circle_trajectory():
    trajectory = circle_trajectory(
        center=(0.0, 0.0),
        radius=1.0,
        steps=100,
    )

    assert len(trajectory) == 100

    for x, y in trajectory:
        distance = math.sqrt(x**2 + y**2)

        assert math.isclose(
            distance,
            1.0,
            abs_tol=1e-9,
        )


def test_circle_trajectory_requires_positive_radius():
    with pytest.raises(ValueError):
        circle_trajectory(
            center=(0.0, 0.0),
            radius=0.0,
        )