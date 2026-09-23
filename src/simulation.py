import matplotlib.pyplot as plt

from src.drawing import create_drawing
from src.kinematics import joint_positions
from src.motion import trajectory_to_angles


def simulate_motion() -> None:
    """Simulate the arm drawing multiple strokes."""

    drawing = create_drawing()

    plt.figure(figsize=(6, 6))

    completed_strokes = []

    for stroke in drawing:
        angles = trajectory_to_angles(stroke)

        x_history = []
        y_history = []

        for theta1, theta2 in angles:
            (x1, y1), (x2, y2) = joint_positions(
                theta1,
                theta2,
            )

            x_history.append(x2)
            y_history.append(y2)

            plt.cla()

            # Tratti già completati
            for completed_x, completed_y in completed_strokes:
                plt.plot(
                    completed_x,
                    completed_y,
                    marker=".",
                )

            # Tratto corrente
            plt.plot(
                x_history,
                y_history,
                marker=".",
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

            plt.xlim(-2.5, 2.5)
            plt.ylim(-2.5, 2.5)

            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("ArmArt - Drawing Simulation")
            plt.grid(True)
            plt.axis("equal")

            plt.pause(0.1)

        completed_strokes.append((x_history, y_history))

    plt.show()


if __name__ == "__main__":
    simulate_motion()
