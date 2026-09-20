import math

import matplotlib.pyplot as plt

from src.kinematics import forward_kinematics


def plot_arm(
    theta1: float,
    theta2: float,
    l1: float = 1.0,
    l2: float = 1.0,
) -> None:
    """Visualize the 2-link robotic arm."""

    x1 = l1 * math.cos(theta1)
    y1 = l1 * math.sin(theta1)

    x2, y2 = forward_kinematics(theta1, theta2, l1, l2)

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
    theta1 = 0.0
    theta2 = math.pi / 2

    plot_arm(theta1, theta2)


if __name__ == "__main__":
    main()