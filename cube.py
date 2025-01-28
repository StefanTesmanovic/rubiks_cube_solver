import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

class RubiksCube:
    ######## start of bulshit chatgpt code that I made work just for the sake of visualising the cube 
    def __init__(self):
        # Define the default color layout of the cube
        self.colors = {
            "U": [["white"] * 3 for _ in range(3)],  # Up face
            "D": [["yellow"] * 3 for _ in range(3)],  # Down face
            "F": [["green"] * 3 for _ in range(3)],  # Front face
            "B": [["blue"] * 3 for _ in range(3)],  # Back face
            "L": [["orange"] * 3 for _ in range(3)],  # Left face
            "R": [["red"] * 3 for _ in range(3)],  # Right face
        }

    def draw_cube(self):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection="3d")

        # Define the positions and orientations of each face
        face_positions = {
            "U": (0, 2, 0),  # Up
            "D": (0, -1, -1),  # Down
            "F": (0, 0, 1),  # Front
            "B": (1, 0, -2),  # Back
            "L": (-1, 0, -1),  # Left
            "R": (2, 0, 0),  # Right
        }
        face_orientations = {
            "U": [(1, 0, 0), (0, 0, -1)],
            "D": [(1, 0, 0), (0, 0, 1)],
            "F": [(1, 0, 0), (0, 1, 0)],
            "B": [(-1, 0, 0), (0, 1, 0)],
            "L": [(0, 1, 0), (0, 0, 1)],
            "R": [(0, 1, 0), (0, 0, -1)],
        }

        for face, (x_offset, y_offset, z_offset) in face_positions.items():
            for i in range(3):
                for j in range(3):
                    color = self.colors[face][i][j]
                    square = self.get_face_square(i, j, x_offset, y_offset, z_offset, face_orientations[face])
                    ax.add_collection3d(Poly3DCollection([square], color=color, edgecolor="black"))

        # Set the limits and remove the axes
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])
        ax.view_init(110, 270)  # Adjust the view angle for better visualization
        ax.axis("off")

        plt.show()

    @staticmethod
    def get_face_square(i, j, x_offset, y_offset, z_offset, orientation):
        right, up = orientation
        origin = (
            x_offset + (j - 1) * right[0] + (1 - i) * up[0],
            y_offset + (j - 1) * right[1] + (1 - i) * up[1],
            z_offset + (j - 1) * right[2] + (1 - i) * up[2],
        )
        square = [
            (
                origin[0] + right[0] * dx + up[0] * dy,
                origin[1] + right[1] * dx + up[1] * dy,
                origin[2] + right[2] * dx + up[2] * dy,
            )
            for dx, dy in [(0, 0), (1, 0), (1, 1), (0, 1)]
        ]
        return square
    #### end of the bullshit code chatgpt code, start of my bullshit code :)
    @staticmethod
    def draw():
        cube = RubiksCube()
        cube.draw_cube()
RubiksCube.draw()
