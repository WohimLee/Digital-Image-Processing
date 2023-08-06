import numpy as np
import matplotlib.pyplot as plt

# Function to find the starting point
def find_starting_point(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] == 1:
                return (i, j)
    return None

# Clockwise direction to move
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Function to find next move
def next_move(position, image, last_direction):
    for i in range(8):
        direction = directions[(i + last_direction) % 8]
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if image[next_position] == 1:
            return next_position, (i + last_direction) % 8
    return None, None

# Function to follow the boundary
def boundary_following(image):
    padded_image = np.pad(image, pad_width=1, mode='constant', constant_values=0)
    starting_point = find_starting_point(padded_image)
    if starting_point is None:
        return []

    boundary = [starting_point]
    last_direction = 0
    current_point = starting_point

    # Iterate until we reach the starting point again
    while True:
        next_point, last_direction = next_move(current_point, padded_image, last_direction)
        if next_point is None or next_point == starting_point:
            break
        boundary.append(next_point)
        current_point = next_point

    return boundary

if __name__ == '__main__':
    # Binary image
    image = np.array([
        [0, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0]
    ])

    boundary = boundary_following(image)

    # Visualize the process
    plt.imshow(image, cmap="gray")
    boundary_x = [p[1] - 1 for p in boundary] # Subtracting 1 to adjust for the padding
    boundary_y = [p[0] - 1 for p in boundary] # Subtracting 1 to adjust for the padding
    plt.plot(boundary_x, boundary_y, 'r')
    plt.show()
