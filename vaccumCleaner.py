import random 
a=[]
booleanStatus = ['clean', 'dirty']
no = 1
n = int(input("Enter number of rooms: "))
for i in range(n):
    nameOfRoom = input(f"Enter name for room {i+1}: ")
    status = input(f"Enter status of room {i+1}: ")
    a.append({
        'name': nameOfRoom,
        'status': status
    })

print("Sequence       Percepts         Actions")

while(True):
    for i in a: 
        if(i['status'] == "clean"):
            print(f"{no}              ({i['name']} {i['status']})        Moving next")
            no = no+1
        elif(i['status'] == "dirty"):
            print(f"{no}              ({i['name']} {i['status']})        Cleaning")
            i["status"] = "clean"
            no = no+1

    temp = int(input("do you want to reperform cleaning? Press 1 to continue Press 0 to exit: "))

    if(temp==0):
        break

    elif(temp==1):
        print("Changing status of rooms...")
        for _ in a:
            rand = random.randint(0,1)
            _['status'] = booleanStatus[rand]
    
    else:
        print("Wrote wrong number breaking from loop....")
        break