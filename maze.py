import pygame
import time

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 1000, 1000  # Window size
ROWS, COLS = 20, 20  # Maze dimensions
CELL_SIZE = WIDTH // COLS  # Size of each cell
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the display window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver with DFS")


# Define the maze as a 2D list (grid)
maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Define the start and end positions
start = (0, 0)
end = (19, 19)

# Function to draw the grid lines and cells
def draw_grid(win, maze):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 1 else BLACK
            pygame.draw.rect(win, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(win, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Function to visualize DFS
def dfs_visual(win, maze, start, end, path=[]):
    # Add the start position to the path
    path = path + [start]

    # Draw the current cell
    pygame.draw.rect(win, RED, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    time.sleep(0.5)  # Slow down to visualize the steps

    # Check if the current position is the end position
    if start == end:
        return path

    # Get the current position's row and column
    row, col = start

    # Define the possible moves (up, down, left, right)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Iterate over each possible move
    for move in moves:
        # Calculate the new position after making the move
        new_row = row + move[0]
        new_col = col + move[1]
        new_pos = (new_row, new_col)

        # Check if the new position is within bounds and is a valid move
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] == 1 and new_pos not in path:
                # Recursively call dfs with the new position
                new_path = dfs_visual(win, maze, new_pos, end, path)
                if new_path:
                    return new_path

    # If no valid moves, backtrack by reverting the cell color
    pygame.draw.rect(win, BLUE, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    time.sleep(0.5)  # Slow down to visualize backtracking

    return None

# Main function to run the visualization
def main():
    run = True
    while run:
        win.fill(BLACK)
        draw_grid(win, maze)
        pygame.display.update()

        # Run the DFS visualization
        solution = dfs_visual(win, maze, start, end)

        # Highlight the final path if found
        if solution:
            for pos in solution:
                pygame.draw.rect(win, GREEN, (pos[1] * CELL_SIZE, pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.display.update()

        # Wait until the user closes the window
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    return

if __name__ == "__main__":
    main()
