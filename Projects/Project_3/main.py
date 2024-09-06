from maze_generator import MazeGenerator
from maze_solver import MazeSolver

# Step 1: Generate the Maze
maze_gen = MazeGenerator(width=21, height=21)
maze = maze_gen.generate_maze()

# Step 2: Solve the Maze
solver = MazeSolver(maze)
start = (1, 1)  # Starting position (x, y)
end = (19, 19)  # Ending position (x, y)

path = solver.solve_maze(start, end)

# Step 3: Display the results
print("Generated Maze:")
maze_gen.display_maze()

if path:
    print("Solution Path:", path)
else:
    print("No path found.")