import pytest

from src.trajectory import line_trajectory


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