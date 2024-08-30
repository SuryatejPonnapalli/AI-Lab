#TEAM MEMBERS
#HU22CSEN0300183 - SURYATEJ
#HU22CSEN0300317 - HARSHITH
#HU22CSEN0300313 - DHANUSH

#OBSERVATION FROM THE EXPERIMENT
# - We implemented Dfs bfs and ucs on map of romania the task being to reach bucharest from arad

#BFS
# - It is complete which means it finds the destination at all cost if the solution exists.
# - It takes comparetively more memory as it covers all nodes at a given level to go to next level.
# - can be optimal if all path has same cost

#DFS
# - It doesn't take path cost into account similar to bfs.
# - It is s memory efficient. 
# - It is not complete as it can go into infinite loop.
# - not optimal.

#UCS
# - It gives the shorted path to the destination with the help of priority queue.
# - It is complete.
# - It can consume alot of memory as it keeps track of all the costs of the nodes.
# - It is optiomal


romaniaMap = {
    'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
    'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}


def dfs(startingNode, endingNode):
    visited = []
    stack = [startingNode]

    while stack:
        # Pop the last element from the stack
        c = stack.pop()
        
        # If the node has not been visited
        if c not in visited:
            # Mark the node as visited
            visited.append(c)
            
            # Check if we have reached the ending node
            if c == endingNode:
                print(f"Reached the destination: {c}")
                return visited
            
            # Add neighbors to the stack
            for neighbor, weight in romaniaMap[c]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    # print(stack) uncomment if you want to view the stack

        
def bfs(startingNode,endingNode):
    visited = []
    queue = [startingNode]
    
    while queue:
        #Popping first element
        c = queue.pop(0)
        
        if c not in visited:
            visited.append(c)

        if c == endingNode:
            print(f"Reached destination: {c}")
            return visited

        for neighbor, weight in romaniaMap[c]:
            if neighbor not in visited:
                queue.append(neighbor)
                # print(queue) uncomment if you want to view the queue
    return visited

def uniform_cost_search(start, goal):
    # Initialize the frontier with the starting node
    frontier = [(0, start)]
    
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
        # Sort the frontier based on the cost
        frontier.sort(key=lambda x: x[0])
        
        # Get the node with the lowest cost
        current_cost, current_city = frontier.pop(0)

        if current_city in visited:
            continue
        
        # Mark the current city as visited
        visited.add(current_city)

        # Check if we have reached the goal
        if current_city == goal:
            break

        # Explore the neighbors of the current city
        for neighbor, weight in romaniaMap[current_city]:
            if neighbor not in visited:
                new_cost = current_cost + weight
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    parent[neighbor] = current_city
                    frontier.append((new_cost, neighbor))

    # Reconstruct the path from the goal to the start
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent.get(goal)

    # Reverse the path to get the correct order
    path.reverse()
    
    return path, cost[path[-1]]

    # Starting City & Destination City
    

if (__name__ == "__main__"):
    print("1)Dfs 2)Bfs 3)Ucs 4)Exit")
    a = int(input("Enter your choice: "))
    if(a == 1):
            visited = dfs("Arad","Bucharest")
            print(visited)
    elif(a == 2):
            visited = bfs("Arad","Bucharest")
            print(visited)
    elif(a == 3):
            path, total_cost = uniform_cost_search('Arad', 'Bucharest')
            print(f"Path: {path}")
            print(f"Total Cost: {total_cost}")
