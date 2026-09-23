import matplotlib.pyplot as plt

from src.drawing import create_drawing
from src.kinematics import joint_positions
from src.motion import trajectory_to_angles


def simulate_motion() -> None:
    """Simulate drawing and travel operations."""

    drawing = create_drawing()

    plt.figure(figsize=(6, 6))

    completed_strokes = []

    for operation in drawing:
        angles = trajectory_to_angles(operation.points)

        current_stroke = []

        for theta1, theta2 in angles:
            (x1, y1), (x2, y2) = joint_positions(
                theta1,
                theta2,
            )

            if operation.operation_type == "DRAW":
                current_stroke.append((x2, y2))

            plt.cla()

            # Tratti già completati
            for stroke in completed_strokes:
                x_points = [point[0] for point in stroke]
                y_points = [point[1] for point in stroke]

                plt.plot(
                    x_points,
                    y_points,
                    marker=".",
                )

            # Tratto corrente
            if operation.operation_type == "DRAW":
                x_points = [point[0] for point in current_stroke]
                y_points = [point[1] for point in current_stroke]

                plt.plot(
                    x_points,
                    y_points,
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

        if operation.operation_type == "DRAW":
            completed_strokes.append(current_stroke)

    plt.show()


if __name__ == "__main__":
    simulate_motion()