#PRIORITY SCHEDULING NON PREEMPTIVE ALGORITHM..

def sort(arr, bt, pr, pid):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(pr[j] > pr[j+1]):
                temp = pr[j]
                pr[j] = pr[j+1]
                pr[j+1] = temp

                temp = bt[j]
                bt[j] = bt[j+1]
                bt[j+1] = temp

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp

    return arr,bt,pr,pid


def checkAllArrived(arr, prev):
    for i in range(len(arr)):
        if(arr[i] <= prev):
            continue
        else:
            return 0
    print("All processes have arrived...")
    
    return 1

def FCFSaccPriority(arr, bt, pr, pid, count, st, ft, ta, prev):
    arr,bt,pr,pid = sort(arr, bt, pr, pid)
    for i in range(len(arr)):
        
        if(count == 0):
        
            count  = 1
            wt[i] = prev - arr[i]
            prev = prev + bt[i]
            print("Waiting time for prcoess",pid[i],"is :",wt[i])
            ft[i] = st[i] + bt[i]
            ta[i] = ft[i] - arr[i]
                        
        else:
            wt[i] = prev - arr[i]
            ft[i] = st[i] + bt[i]
            ta[i] = ft[i] - arr[i]                   
            prev = prev + bt[i]
            print("Waiting time for prcoess",pid[i],"is :",wt[i])
            
        
    
    


def deleteProc(i, arr, bt, pr, pid, wt):

    del arr[i]
    del bt[i]
    del pr[i]
    del pid[i]
    
    return arr, bt, pr, pid

def priorityWoPreemption(arr, bt, pr, pid, wt):
    arr,bt,pr,pid = sort(arr, bt, pr, pid)
    prev = min(arr)
    temp_pid = pid.copy()
    count = 0
    st = [0]*len(arr)
    ft = [0]*len(arr)
    ta = [0]*len(arr)

    while(len(arr) != 0):
        
        if(checkAllArrived(arr, prev)):
            FCFSaccPriority(arr, bt, pr, pid, count, st, ft, ta, prev)
            return wt,ta,temp_pid
        for i in range(len(arr)):
            
            
            if(arr[i] <= prev):
                
                if(count == 0):
                    st[i] = arr[i] 
                    wt[i] = prev - arr[i]
                    prev = prev + bt[i]
                    count = 1
                    print("Waiting time for prcoess",pid[i],"is :",wt[i])
        
                    ft[i] = st[i] + bt[i]
                    ta[i] = ft[i] - arr[i]
                    
                else:
                    wt[i] = prev - arr[i]
                    ft[i] = st[i] + bt[i]
                    ta[i] = ft[i] - arr[i]                   
                    prev = prev + bt[i]
                    print("Waiting time for prcoess",pid[i],"is :",wt[i])
                arr,bt,pr,pid = deleteProc(i, arr, bt, pr, pid, wt)
            elif(arr[i] > prev):
                
                j = i
                while(arr[j] > prev and j<len(arr)):
                    j = j + 1
                k = min(arr)
                while(k > prev):
                    prev = prev + 1
                if(arr[j] <= prev):
                    
                    if(count == 0):
                        count = 1
                        st[j] = arr[j] 
                        wt[j] = prev - arr[j]
                        prev = prev + bt[j]
                        print("Waiting time for prcoess",pid[j],"is :",wt[j])
                        ft[j] = st[j] + bt[j]
                        ta[j] = ft[j] - arr[j]
                    else:
                        wt[j] = prev - arr[j]
                        ft[j] = st[j] + bt[j]
                        ta[j] = ft[j] - arr[j]                   
                        prev = prev + bt[j]
                        print("Waiting time for prcoess",pid[j],"is :",wt[j])
                    arr,bt,pr,pid = deleteProc(j, arr, bt, pr, pid, wt)
            if(checkAllArrived(arr, prev)):
                FCFSaccPriority(arr, bt, pr, pid, count, st, ft, ta, prev)
                return wt,ta,temp_pid
            
            

    
    return wt,ta,temp_pid
    

arr = [2,4,5]
wt = [0]*len(arr)
bt = [5,2,1]
pr = [3,2,1]
pid = ['p1', 'p2', 'p3']
wt,ta,temp_pid = priorityWoPreemption(arr, bt, pr, pid, wt)
avg_wt = sum(wt)/len(wt)
print("The average waiting time is: ",avg_wt)




''' EXAMPLE:
PROCESS-ID   ARRIVAL-TIME   BURST-TIME   PRIORITY    
    P1           2             5            3

    P2           4             2            2

    P3           5             1            1
'''











