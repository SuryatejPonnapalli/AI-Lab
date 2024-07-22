import pandas as pd
import random

def main():
    percept_sequence = input("Enter sequence of percepts (e.g., 'c c c d c'): ").strip().split()
    environment_model = []
    cleanRoom(percept_sequence,environment_model)
    print(percept_sequence)
    for i in environment_model:
        print(i)


def cleanRoom(percept_sequence,environment_model):
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
            environment_model.append({
            "Room_Number": room_number,
            "Status": "Clean",
            "Pervious_Action": "Cleaning"
        })
        else:
            action = "moving next"
            action_array.append(action)
            environment_model.append({
            "Room_Number": room_number,
            "Status": "Clean",
            "Pervious_Action": "Was Clean"
        })

        
    data = {'Percepts': result_array, "Actions": action_array}
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()