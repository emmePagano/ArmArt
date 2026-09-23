import matplotlib.pyplot as plt

from src.kinematics import joint_positions
from src.motion import trajectory_to_angles
from src.trajectory import circle_trajectory


def simulate_motion() -> None:
    """Simulate the arm following a straight-line trajectory."""

    trajectory = circle_trajectory(
    center=(0.7, 0.8),
    radius=0.3,
    steps=100,
)
    

    angles = trajectory_to_angles(trajectory)

    x_history = []
    y_history = []

    plt.figure(figsize=(6, 6))

    for theta1, theta2 in angles:
        (x1, y1), (x2, y2) = joint_positions(
            theta1,
            theta2,
        )

        x_history.append(x2)
        y_history.append(y2)

        plt.cla()

        # Traiettoria desiderata
        plt.plot(
            [point[0] for point in trajectory],
            [point[1] for point in trajectory],
            linestyle="--",
            label="Traiettoria desiderata",
        )

        # Braccio
        plt.plot(
            [0, x1],
            [0, y1],
            marker="o",
        )

        plt.plot(
            [x1, x2],
            [y1, y2],
            marker="o",
        )

        # Traiettoria effettiva della punta
        plt.plot(
            x_history,
            y_history,
            marker=".",
            label="Traiettoria effettiva",
        )

        plt.xlim(-2.5, 2.5)
        plt.ylim(-2.5, 2.5)

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("ArmArt - Motion Simulation")
        plt.grid(True)
        plt.axis("equal")
        plt.legend()

        plt.pause(0.1)

    plt.show()


if __name__ == "__main__":
    simulate_motion()