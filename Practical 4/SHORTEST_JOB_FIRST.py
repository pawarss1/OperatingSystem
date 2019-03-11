#SHORTEST JOB FIRST..

arr = [1, 2, 3]
bt = [5, 7, 4]
pid = ['P1','P2','P3']
wt = [0]*len(arr)
ft = [0]*len(arr)
ta = [0]*len(arr)
st = [0]*len(arr)



def sort():
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(bt[j] > bt[j+1]):
                temp = bt[j]
                bt[j] = bt[j+1]
                bt[j+1] = temp

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

                temp = pid[j]
                pid[j] = pid[j+1]
                pid[j+1] = temp

def checkAllArrived(prev):
    for i in range(len(arr)):
        if(arr[i] <= prev):
            continue
        else:
            return 0
    print("All processes have arrived...")
    
    return 1

def FCFSaccBurst(prev):
    sort()
    for i in range(len(arr)):
        wt[i] = prev - arr[i]
        prev = prev + bt[i]
        print("Waiting time for prcoess",pid[i],"is :",wt[i])
        ft[i] = st[i] + bt[i]
        ta[i] = ft[i] - arr[i]


def deleteProc(i):
    del arr[i]
    del bt[i]
    del pid[i]



    
def sjf():
    prev = min(arr)
    sort()
    temp_pid = pid.copy()
    
    while(len(arr) != 0):
        if(checkAllArrived(prev)):
            FCFSaccBurst(prev)
            return wt,ta,temp_pid


        for i in range(len(arr)):

            if(arr[i] > prev):
                 j = i 
                 
                 while(arr[j] > prev and j < len(arr)):
                     j += 1
                     if(j == len(arr)):
                         break
                 
                 if(arr[j] <= prev):
                     wt[j] = prev - arr[j]
                     prev = prev + bt[j]
                     print("Waiting time for prcoess",pid[j],"is :",wt[j])

                     deleteProc(j)
                
            elif(arr[i] <= prev):
                wt[i] = prev - arr[i]
                print("Waiting time for prcoess",pid[i],"is :",wt[i])
                
                deleteProc(i)

            else:
                k = min(arr)
                while(prev < k):
                    prev = prev + 1
                    
            if(checkAllArrived(prev)):
                FCFSaccBurst(prev)
                return wt,ta,temp_pid

wt, ta, temp_pid = sjf()
avg_wt = sum(wt)/len(wt)
print("The average waitning time is: ", avg_wt)




''' EXAMPLE:
PROCESS-ID   ARRIVAL-TIME   BURST-TIME     
    P1           1             5            

    P2           2             7            

    P3           3             4            
'''



