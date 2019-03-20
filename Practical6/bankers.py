#BANKERS ALGORITHM..

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
#counter = process
running = [1]*process 
available = [3, 3, 2]
maxAvailable = [10, 5, 7]

need = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
]
safe = 0

for i in range(process):
    for j in range(resources):
        need[i][j] = maxNeed[i][j] - allocated[i][j]

def breakWhileUnsafeState():
    safe = not safe



def bankers(counter):
    #print(need)
    deadlockCtr = 0
    flag = 0
    while(counter != 0):
        safe = 0
        for i in range(process):
            deadlockCtr = counter
            if(running[i]):
                flag = 1
                
                for j in range(resources):
                    if(need[i][j] > available[j]):
                        flag = 0
                        
                    if(not flag):
                        deadlockCtr -=1
                        if(deadlockCtr == 0):
                            breakWhileUnsafeState()
                            return -1
                    else:
                        break
                    
                if(flag):
                    print("Process", i, " is executing")
                    running[i] = 0
                    safe = 1
                    counter = counter - 1
                
                    for j in range(resources):
                        available[j] += allocated[i][j]
                    print("AVAILABLE RESOURCES AFTER PROCESS ",i, "ARE", available)
                    break

    if(safe):
        print("The processes are in safe state")
        print(available)
    
    elif(not safe):
        print("The processes are not in safe state")

counter = 5
result = bankers(counter)
if(result == -1):
    print("The processes are not in safe state")
