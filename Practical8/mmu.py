#Memory Mangement Unit: Best fit, Worst fit, First fit..
processSize = [212, 417, 112, 426]
memBlocksSizeInit = [100, 500, 200, 300, 600]

process = len(processSize)
blocks = len(memBlocksSizeInit)


def PrintProcess(allocation,memBlocksSize, a):
    print(a)
    for i in range(process):
        if(allocation[i] == -1):
            print("Process ", i+1,"of size",processSize[i],"assignment not possible")
        else:
            print("Process ", i+1,"of size",processSize[i], "MB assigned Block Number", allocation[i]+1)
        






def bestFit(memBlocksSize):
    allocation = [-1]*(len(processSize))

    for i in range(process):
        bestFitIndex = -1
        for j in range(blocks):
            
            if(memBlocksSize[j] >= processSize[i]):
                if(bestFitIndex == -1):
                    bestFitIndex = j
                elif(memBlocksSize[j] < memBlocksSize[bestFitIndex] ):
                    bestFitIndex = j

        if(bestFitIndex != -1):
            allocation[i] = bestFitIndex
            memBlocksSize[bestFitIndex] -= processSize[i]
    
    PrintProcess(allocation, memBlocksSize, "Best Fit")

def firstFit(memBlocksSize):
    allocation = [-1]*(len(processSize))

    for i in range(process):
        for j in range(blocks):
            if(memBlocksSize[j] >= processSize[i]):
                allocation[i] = j
                memBlocksSize[j] -= processSize[i]
                break
    
    PrintProcess(allocation,memBlocksSize, "First Fit")


def worstFit(memBlocksSize):
    allocation = [-1]*(len(processSize))
    #print(memBlocksSize)

    for i in range(process):
        worstFitIndex = -1
        for j in range(blocks):
            if(memBlocksSize[j] >= processSize[i]):
                if(worstFitIndex == -1):
                    worstFitIndex = j
                elif(memBlocksSize[j] > memBlocksSize[worstFitIndex] ):
                    worstFitIndex = j

        if(worstFitIndex != -1):
            allocation[i] = worstFitIndex
            #print(allocation[i])
            memBlocksSize[worstFitIndex] -= processSize[i]
    
    PrintProcess(allocation, memBlocksSize, "Worst Fit")


memBlocksSize = memBlocksSizeInit.copy()
bestFit(memBlocksSize)

memBlocksSize = memBlocksSizeInit.copy()
firstFit(memBlocksSize)

memBlocksSize = memBlocksSizeInit.copy()
worstFit(memBlocksSize)
