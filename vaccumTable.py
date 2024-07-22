import pandas as pd

percept_sequence = input("Enter sequence of percepts (e.g., 'c c c d c'): ").strip().split()

result = ""
result_array = []
action_array = []

for i, percept in enumerate(percept_sequence):
    room_number = i + 1  
    result += f"{room_number}{percept} "
    result_array.append(result.strip())

    if percept == "d":
        action = "cleaning"
        action_array.append(action)
        percept_sequence[i] = "c"
        result += f"{room_number}c "
        result_array.append(result.strip())
        action = "moving next"
        action_array.append(action)
    else:
        action = "moving next"
        action_array.append(action)

data = {'Percepts': result_array, "Actions": action_array}
df = pd.DataFrame(data)

print(df)

