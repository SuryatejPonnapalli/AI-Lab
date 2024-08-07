#TEAM MEMBERS
#HU22CSEN0300183 P SURYATEJ
#HU22CSEN0300317 P SAI HARSHITH
#HU22CSEN0300313 K DHANUSH KUMAR
#Observation from the assignment
#We have mapped out a tree representing all possible scenarios for transporting a man, goat, tiger, and cabbage. To explore these scenarios, we implemented a breadth-first search (BFS) algorithm, taking advantage of the limited number of cases and the low space it takes to implement logiuc. We thoroughly analyzed all possible scenarios to ensure the algorithm's efficiency. It is crucial for the machine to keep track of the pieces locations and make decisions based on a comprehensive understanding of all potential cases.


initial_state = ('L', 'L', 'L', 'L')
goal_state = ('R', 'R', 'R', 'R')

def is_valid_state(state):
    M, T, G, C = state
    if (T == G != M) or (G == C != M):
        return False
    return True

def get_possible_moves(state):
    M, T, G, C = state
    moves = []

    if M == 'L':
        moves.append(('R', T, G, C))  
        if T == 'L': moves.append(('R', 'R', G, C)) 
        if G == 'L': moves.append(('R', T, 'R', C))  
        if C == 'L': moves.append(('R', T, G, 'R'))  
    else:
        moves.append(('L', T, G, C))  
        if T == 'R': moves.append(('L', 'L', G, C))  
        if G == 'R': moves.append(('L', T, 'L', C)) 
        if C == 'R': moves.append(('L', T, G, 'L')) 

    valid_moves = []
    for move in moves:
        if is_valid_state(move):
            valid_moves.append(move)
    return valid_moves

def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        current_state, path = queue.pop(0)
        if current_state == goal:
            return path

        for move in get_possible_moves(current_state):
            if move not in visited:
                visited.add(move)
                queue.append((move, path + [move]))

    return None

solution_path = bfs(initial_state, goal_state)

if solution_path:
    print("Solution path:")
    for state in solution_path:
        print(state)
else:
    print("No solution found.")
