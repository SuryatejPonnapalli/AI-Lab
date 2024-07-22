import random
import math
import pandas as pd


m = random.randint(8,15)
n = random.randint(8,15)
area = m * n
result = " "
result_array = []

no_of_squares = math.ceil(area/10)

array_of_status_of_squares = []

action = " "
action2 = " "
action_array = []

for i in range (1,no_of_squares+1):
    rand = random.randint(1,20)
    if(rand == 2):
        array_of_status_of_squares.append({
            "room_number": i,
            "room_status": "d"
        })
    else:
        array_of_status_of_squares.append({
            "room_number": i,
            "room_status": "c"
        })

for i in array_of_status_of_squares:
         result = result + f"{i['room_number']}{i['room_status']} "
         result_array.append(result)
         if(i["room_status"] == "d"):
                i["room_status"] == "c"
                result = result + f"{i['room_number']}c "
                result_array.append(result)
                action = "cleaning"
                action2 = "moving next"
                action_array.append(action)
                action_array.append(action2)
         else:
            action = "moving next"
            action_array.append(action)

data = {'Percepts':result_array,
        "Actions": action_array
        }

df = pd.DataFrame(data)

print(df)