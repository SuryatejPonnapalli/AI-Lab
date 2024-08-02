#TEAM MEMBERS
#HU22CSEN0300183 P SURYATEJ
#HU22CSEN0300317 P SAI HARSHITH
#HU22CSEN0300313 K DHANUSH KUMAR
#Observation from the assignment
#We have understood how model based and goal based agent work
#we take the percept history and create model of the envionment so that 
#vaccum cleaner can even work in partial observable environments as well
#We have given goal that it cleans all the rooms
#Even if the vaccum cleaner doesnt have sensor it can work based on the model created of the environment


import random

#Condition action table for the vaccum cleaner
action_table = {
    ('A', 'd'): ('clean', 'A', 'c'),  
    ('A', 'c'): ('do nothing', 'A', 'c'),  
    ('B', 'd'): ('clean', 'B', 'c'), 
    ('B', 'c'): ('do nothing', 'B', 'c'), 
}

#it generates or cleans dirt upon going to next room for 10 iterations
def get_random_room_state():
    return random.choice(['c', 'd'])

#keeping track of percept history so that the vaccum cleaner can work efficiently and creating model which has all percepts
percept_history = []
do_nothing_count = 0
consecutive_do_nothing = 1

#taking initial percept from user
current_percept_input = input("Enter current percept (e.g., 'A c'): ").strip().split()
current_state = (current_percept_input[0], current_percept_input[1])

for i in range(10):
    location, room_state = current_state

    #getting the action based on current location and room state
    actions = action_table.get((location, room_state), ('do nothing',))
    action = actions[0]

    #adding it to percept history for future uses
    percept_history.append(current_state)

    if action == 'clean':
        current_state = (location, 'c')
        print(f"Location = {location}, State = {room_state}, Action = {action}, internal state = {current_state}")
        consecutive_do_nothing = 1
    elif action == 'do nothing':
        #if the action is to do nothing, increment the consecutive do nothing counter
        print(f"Location = {location}, State = {room_state}, Action = {action}, internal state = {current_state}")
        consecutive_do_nothing += 1

        #if agent does nothing 2 consecutive times then move from one room to another 
        if consecutive_do_nothing == 2:  
            if location == 'A':
                print(f"Location = A, State = {room_state}, Action = move right, internal state = {current_state}")
                current_state = ('B', get_random_room_state())
            elif location == 'B':
                print(f"Location = B, State = {room_state}, Action = move left, internal state = {current_state}")
                current_state = ('A', get_random_room_state())
            consecutive_do_nothing = 1

#printing the percept history and the final position of the vacuum cleaner
#It shows that vaccum cleaner knows its present state and can work in partial observable environments
print("\nPercept History:", percept_history)
print(f"vaccum cleaner current position {current_state}")
