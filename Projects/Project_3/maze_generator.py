import random
import numpy as np

class MazeGenerator:
    def __init__(self, width, height):
        """
        Initialize the maze with given width and height.
        The maze grid is a 2D array where 0 represents a wall and 1 represents a path.
        """
        self.width = width if width % 2 == 1 else width + 1  # Ensure odd dimensions
        self.height = height if height % 2 == 1 else height + 1
        self.grid = np.zeros((self.height, self.width), dtype=int)

    def generate_maze(self, start_x=1, start_y=1):
        """
        Start the maze generation process using recursive backtracking.
        """
        self.grid[start_y][start_x] = 1  # Mark the start point as a path
        self._recursive_backtracking(start_x, start_y)
        return self.grid

    def _recursive_backtracking(self, x, y):
        """
        Private method to perform recursive backtracking for maze generation.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
        random.shuffle(directions)  # Randomize direction to create a unique maze

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy

            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 0:
                self.grid[ny][nx] = 1  # Carve the new path
                self.grid[y + dy][x + dx] = 1  # Carve the wall between current and next
                self._recursive_backtracking(nx, ny)

    def display_maze(self):
        """
        Display the generated maze using matplotlib (optional for testing/visualization).
        """
        import matplotlib.pyplot as plt
        plt.imshow(self.grid, cmap='binary')
        plt.show()