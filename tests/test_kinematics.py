import math

from src.kinematics import forward_kinematics


def test_forward_kinematics_straight():
    x, y = forward_kinematics(0, 0)

    assert math.isclose(x, 2.0)
    assert math.isclose(y, 0.0)


def test_forward_kinematics_right_angle():
    x, y = forward_kinematics(0, math.pi / 2)

    assert math.isclose(x, 1.0)
    assert math.isclose(y, 1.0)