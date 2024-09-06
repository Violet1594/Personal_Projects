from collections import deque

class MazeSolver:
    def __init__(self, maze):
        """
        Initialize the solver with the generated maze.
        The maze is a 2D array where 0 represents a wall and 1 represents a path.
        """
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

    def solve_maze(self, start, end):
        """
        Solve the maze using BFS and return the path from start to end.
        """
        path = self._bfs(start, end)
        return path

    def _bfs(self, start, end):
        """
        Private method to perform Breadth-First Search (BFS) to find the shortest path.
        """
        queue = deque([start])
        visited = set()
        visited.add(start)
        came_from = {start: None}  # To reconstruct the path

        while queue:
            current = queue.popleft()

            if current == end:
                return self._reconstruct_path(came_from, end)

            for neighbor in self._get_neighbors(current):
                if neighbor not in visited and self.maze[neighbor[1]][neighbor[0]] == 1:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

        return None  # If no path is found

    def _get_neighbors(self, position):
        """
        Get the neighboring cells (N, E, S, W) that are valid paths.
        """
        x, y = position
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((nx, ny))

        return neighbors

    def _reconstruct_path(self, came_from, current):
        """
        Reconstruct the path from the BFS search.
        """
        path = []
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()  # Reverse to get the correct order
        return path