import argparse
import math

import matplotlib.pyplot as plt

from src.kinematics import joint_positions


def plot_arm(
    theta1: float,
    theta2: float,
    l1: float = 1.0,
    l2: float = 1.0,
) -> None:
    """Visualize the 2-link robotic arm."""

    (x1, y1), (x2, y2) = joint_positions(
        theta1, theta2, l1, l2
    )

    plt.figure(figsize=(6, 6))

    plt.plot([0, x1], [0, y1], marker="o")
    plt.plot([x1, x2], [y1, y2], marker="o")

    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("ArmArt - 2D Robotic Arm")
    plt.grid(True)
    plt.axis("equal")

    plt.savefig("outputs/arm.png")
    plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simulate the ArmArt robotic arm."
    )

    parser.add_argument(
        "--theta1",
        type=float,
        default=0.0,
        help="First joint angle in degrees.",
    )

    parser.add_argument(
        "--theta2",
        type=float,
        default=90.0,
        help="Second joint angle in degrees.",
    )

    args = parser.parse_args()

    theta1 = math.radians(args.theta1)
    theta2 = math.radians(args.theta2)

    plot_arm(theta1, theta2)


if __name__ == "__main__":
    main()