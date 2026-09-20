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

from src.kinematics import joint_positions


def test_joint_positions_right_angle():
    (x1, y1), (x2, y2) = joint_positions(
        0, math.pi / 2
    )

    assert math.isclose(x1, 1.0)
    assert math.isclose(y1, 0.0)

    assert math.isclose(x2, 1.0)
    assert math.isclose(y2, 1.0)