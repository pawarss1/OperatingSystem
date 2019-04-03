allocated = [[0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
]

maxNeed = [[7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 4, 3]
]

process = 5
resources = 3
counter = process
running = [1]*len(process) 
available = [3, 3, 2]
need = [0]*len(maxNeed)
safe = 0

for i in range(process):
    for j in range(resources):
        need[i][j] = maxNeed[i][j] - allocated[i][j]




def bankers():
    flag = 0
    while(counter != 0):
        safe = 0
        for i in range(process):
            if(running[i]):
                flag = 1
                for j in range(resources):
                    if(maxNeed[i][j] - allocated[i][j] > available[j]):
                        flag = 0
                        break
                
                if(flag):
                    print("Process", i+1, " is executing")
                    running[i] = 0
                    safe = 1
                    counter = counter - 1

                    for j in range(resources):
                        available[j] += allocated[i][j]
                    break

    if(safe):
        print("The processes are in safe state")
    elif(not safe):
        print("The processes are not in safe state")


bankers()