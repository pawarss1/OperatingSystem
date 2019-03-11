#ROUND ROBIN SCHEDULING ALGORITHM..

import queue as q
q = q.Queue(maxsize = 10)

arr = [2,1,0,3]
bt= [5,4,10,3]
pid = ['P3','P2','P1','P4']
quan = 3

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

    

def roundRobin():
    
    sort()

    rem_bt = bt.copy()
    t = 0
    wt = [0]*len(arr)
    seq = ['P1']*len(list(q.queue))
    i = 0
    if(rem_bt[i] > quan):
        rem_bt[i] = rem_bt[i] - quan
        t = t + quan    
        j = i + 1
        while(arr[j] <= t and (j <len(arr))):
            q.put(pid[j])
            
            j = j + 1
            if(j == len(arr)):
               break
        q.put(pid[i])
        
        
    elif(rem_bt[i] <= quan):
        t = t + rem_bt[i]
        wt[i] = t - bt[i] - arr[i]
        
        rem_bt[i] = 0
        
        j = i + 1
        while(arr[j] <= t and j < len(arr)):
            q.put(pid[j])
            j = j + 1
            if(j == len(arr)):
               break
        if(rem_bt[i] != 0):
            q.put(pid[i])
    seq.append(pid[i])

    while(not q.empty()):
        i = pid.index(q.get())
        seq.append(pid[i])
        if(rem_bt[i] > quan):
            rem_bt[i] = rem_bt[i] - quan
            
            t = t + quan
            j = i + 1
            if(len(arr) == j):
                continue
            while(arr[j] <= t and j < len(arr) and (rem_bt[j] != 0)):
                
                if(pid[j] not in list(q.queue)):
                    q.put(pid[j])
                   
                j = j + 1
                if(j == len(arr)):
                    break
            q.put(pid[i])
            
          
        elif(rem_bt[i] <= quan):
                t = t + rem_bt[i]
                rem_bt[i] = 0
                wt[i] = t - bt[i] - arr[i]
                j = i + 1
                if(len(arr) == j):
                    continue
                while(arr[j] <= t and j <len(arr) and (rem_bt[j] != 0)):
                    if(pid[j] not in list(q.queue)):
                        q.put(pid[j])
                    j = j + 1
                    if(j == len(arr)):
                        break
                if(rem_bt[i] != 0):
                    q.put(pid[i])
                else:
                    continue
         
    return seq,wt
    
seq,wt = roundRobin()
print("Sequence of operations is: ",seq)

for i in range(len(wt)):
    print("The waiting time for process",pid[i],"is: ",wt[i])

avg_wt = sum(wt)/len(wt)
print("The average waiting time is: ", avg_wt)

''' EXAMPLE:
quantum tim = 3
PROCESS-ID   ARRIVAL-TIME   BURST-TIME      
    P1           0            10           

    P2           1             4            

    P3           2             5            

    P4           3             3
'''




