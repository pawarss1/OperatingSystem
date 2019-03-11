#FIRST CUM FIRST SERVE ALGO..


arr = [1,3,2,5,4]
bt = [2,4,1,3,2]
pid = ['P1','P2','P3','P4','P5']

wt = [0]*len(arr)

def sort():
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                temp = bt[j]
                bt[j] = bt[j+1]
                bt[j+1] = temp

                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp


def fcfs():
    prev = min(arr)
    temp = 0
    count = 0
    sort()
    for i in range(len(arr)):
        if(count == 0):
            wt[0] = 0
            count = 1
            print("The waiting time for process",pid[i],"is: ",wt[i])
            prev = prev + bt[i]
        else:
            if(arr[i] > prev):
                while(arr[i] != prev):
                    prev = prev + 1
            wt[i] = prev - arr[i]
            prev = prev + bt[i]
            print("The waiting time for process",pid[i],"is: ",wt[i])
    return wt

wt = fcfs()
avg_wt = sum(wt)/len(wt)
print("The average waiting time is: ",avg_wt)

''' EXAMPLE:
PROCESS-ID   ARRIVAL-TIME   BURST-TIME   
    P1           1             2            

    P2           3             4            

    P3           2             1            
    
    P4           5             3
    
    P5           4             2
'''

