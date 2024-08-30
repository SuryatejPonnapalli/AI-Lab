#TEAM 
#HU22CSEN0300313 K DHANUSH KUMAR
#HU22CSEN0300183 P SURYATEJ
#HU22CSEN0300317 POLI SAI HARSHITH

# This is a code that we have written for A*
# The efficiency and optimality of A* are highly dependent on the heuristic used. If the heuristic is not well-designed (i.e., it overestimates or underestimates the actual cost), A* might not find the most efficient route.
# A* is particularly useful in scenarios where speed is more critical than absolute optimality, such as real-time systems, video games, or situations where finding a "good enough" solution quickly is more important than finding the perfect one.
# Your observation that A* is a fast algorithm but sometimes does not yield the most efficient route is valid, especially if the heuristic is not perfectly aligned with the actual cost. It’s an excellent choice when quick decision-making is prioritized over finding the absolute best route.


romaniaMap = {
    'Arad': {
        'connections': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
        'hsld': 366  
    },
    'Zerind': {
        'connections': [('Arad', 75), ('Oradea', 71)],
        'hsld': 374  
    },
    'Oradea': {
        'connections': [('Zerind', 71), ('Sibiu', 151)],
        'hsld': 380  
    },
    'Sibiu': {
        'connections': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
        'hsld': 253  
    },
    'Timisoara': {
        'connections': [('Arad', 118), ('Lugoj', 111)],
        'hsld': 329  
    },
    'Lugoj': {
        'connections': [('Timisoara', 111), ('Mehadia', 70)],
        'hsld': 244  
    },
    'Mehadia': {
        'connections': [('Lugoj', 70), ('Drobeta', 75)],
        'hsld': 241  
    },
    'Drobeta': {
        'connections': [('Mehadia', 75), ('Craiova', 120)],
        'hsld': 242  
    },
    'Craiova': {
        'connections': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
        'hsld': 160  
    },
    'Rimnicu': {
        'connections': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
        'hsld': 193  
    },
    'Fagaras': {
        'connections': [('Sibiu', 99), ('Bucharest', 211)],
        'hsld': 176  
    },
    'Pitesti': {
        'connections': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
        'hsld': 100  
    },
    'Bucharest': {
        'connections': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
        'hsld': 0  
    },
    'Giurgiu': {
        'connections': [('Bucharest', 90)],
        'hsld': 77  
    },
    'Urziceni': {
        'connections': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
        'hsld': 80  
    },
    'Hirsova': {
        'connections': [('Urziceni', 98), ('Eforie', 86)],
        'hsld': 317  
    },
    'Eforie': {
        'connections': [('Hirsova', 86)],
        'hsld': 161  
    },
    'Vaslui': {
        'connections': [('Iasi', 92), ('Urziceni', 142)],
        'hsld': 199  
    },
    'Iasi': {
        'connections': [('Vaslui', 92), ('Neamt', 87)],
        'hsld': 226  
    },
    'Neamt': {
        'connections': [('Iasi', 87)],
        'hsld': 234  
    }
}


def a_star_search(start, goal):
    # Initialize the frontier with the starting node and its heuristic cost
    frontier = [(romaniaMap[start]['hsld'], 0, start)]
    
    # Visited set to keep track of visited nodes
    visited = set()
    
    # Parent dictionary to reconstruct the path
    parent = {}
    
    # Cost dictionary to store the cost to reach each node
    cost = {}
    for city in romaniaMap:
        cost[city] = float('inf')
    
    # Cost to reach the starting node is 0
    cost[start] = 0

    while len(frontier) > 0:
        # Sort the frontier based on the total cost (actual cost + heuristic)
        frontier.sort(key=lambda x: x[0])
        
        # Get the node with the lowest total cost
        _, current_cost, current_city = frontier.pop(0)

        if current_city in visited:
            continue
        
        # Mark the current city as visited
        visited.add(current_city)

        # Check if we have reached the goal
        if current_city == goal:
            break

        # Explore the neighbors of the current city
        for neighbor, weight in romaniaMap[current_city]['connections']:
            if neighbor not in visited:
                new_cost = current_cost + weight
                heuristic_cost = new_cost + romaniaMap[neighbor]['hsld']
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    parent[neighbor] = current_city
                    frontier.append((heuristic_cost, new_cost, neighbor))

    # Reconstruct the path from the goal to the start
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent.get(goal)

    # Reverse the path to get the correct order
    path.reverse()
    
    return path, cost[path[-1]]

# Example usage
start_city = input("Enter your start city")
goal_city = input("Enter your end city")
path, cost = a_star_search(start_city, goal_city)
print(f"Path: {path}, Total Cost: {cost}")
