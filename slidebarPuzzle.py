#BFS start
# from collections import deque

# # Define the goal state
# goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))  # 0 represents the empty tile

# # Define directions for moving the empty tile (row_change, column_change)
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1)
# }

# def find_empty_tile(state):
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == 0:
#                 return i, j

# def get_neighbors(state):
#     neighbors = []
#     x, y = find_empty_tile(state)
#     for move, (dx, dy) in directions.items():
#         new_x, new_y = x + dx, y + dy
#         if 0 <= new_x < 3 and 0 <= new_y < 3:
#             new_state = [list(row) for row in state]
#             new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
#             neighbors.append(tuple(tuple(row) for row in new_state))
#     return neighbors

# def bfs(start_state):
#     if start_state == goal_state:
#         return []
    
#     queue = deque([(start_state, [])])
#     visited = set()
#     visited.add(start_state)
    
#     while queue:
#         current_state, path = queue.popleft()
        
#         for neighbor in get_neighbors(current_state):
#             if neighbor not in visited:
#                 new_path = path + [neighbor]
#                 if neighbor == goal_state:
#                     return new_path
#                 queue.append((neighbor, new_path))
#                 visited.add(neighbor)
    
#     return None  # No solution found

# def get_user_input():
#     print("Enter the 3x3 puzzle state row by row (use 0 for the empty tile):")
#     state = []
#     for i in range(3):
#         row = input(f"Enter row {i + 1} (e.g., '1 2 3'): ").strip().split()
#         if len(row) != 3:
#             raise ValueError("Each row must have exactly 3 numbers.")
#         state.append(tuple(int(num) for num in row))
#     return tuple(state)

# # Example usage
# try:
#     start_state = get_user_input()
#     if len(start_state) != 3 or any(len(row) != 3 for row in start_state):
#         raise ValueError("The puzzle state must be a 3x3 grid.")
    
#     solution = bfs(start_state)

#     if solution:
#         print("Solution path:")
#         for step in solution:
#             for row in step:
#                 print(row)
#             print("-----")
#     else:
#         print("No solution found.")
# except ValueError as e:
#     print(f"Input error: {e}")

import heapq

# Define the goal state
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))  # 0 represents the empty tile

# Define directions for moving the empty tile (row_change, column_change)
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = divmod(value - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = find_empty_tile(state)
    for move, (dx, dy) in directions.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()
    
    while open_set:
        estimated_cost, cost, current_state, path = heapq.heappop(open_set)
        if current_state == goal_state:
            return path
        
        if current_state in visited:
            continue
        visited.add(current_state)
        
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(open_set, (cost + 1 + manhattan_distance(neighbor), cost + 1, neighbor, new_path))

    return None  # No solution found

# Example usage
start_state = ((1, 2, 3), (4, 5, 6), (0, 7, 8))  # Modify this to your initial state
solution = a_star(start_state)

if solution:
    for step in solution:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution found.")
