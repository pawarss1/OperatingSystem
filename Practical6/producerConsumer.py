
#PRODUCER-CONSUMER ALGO..

import time


empty = 5
full = 0

semaphore = True

def producer():
    time.sleep(3)
    global semaphore
    global empty
    global full
    
    j = 0
    while(not semaphore):
        print("Consumer consuming cant produce")
        j +=1
        if(j > 5):
            semaphore = True
            print("Consuming a process done...Now can produce")
            return

    print("Producer acquiring semaphore")
    if(full == 0):
        semaphore = False
        full += 1
        empty -=1
        consumer()
        print("First Process Produced..")
    

    else:
        semaphore = False
        empty -= 1
        full += 1
        print("Process produced..")
    semaphore = True
    print("\n")



def consumer():
    time.sleep(3)
    global semaphore
    global empty
    global full
    
    j = 0
    while(not semaphore):
        print("Producer producing cant consume")
        j +=1
        if(j > 5):
            semaphore = True
            print("Producing a process done...Now can consume")
            return 

    print("Consurmer acquiring semaphore")

    if(full == 0):
        semaphore = False
        print("Nothing to consume..")
    elif(empty == 4):
        semaphore = False
        producer()
        print("First Process consumed..")
    
    else:
        empty += 1
        full -= 1
        print("Process Consumed...")
    semaphore = True
    print("\n")


    
producer()

consumer()
producer()
producer()
producer()

consumer()
consumer()
