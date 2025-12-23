# Managing Process with values
# While the Queue you saw previously sends data through a "tunnel" (pipes), a Value creates a specific spot in memory that multiple processes can access and modify directly.

from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100_000):
        with counter.get_lock(): #Every Value object comes with a built-in lock.
            #Prevents multiple processes from corrupting the shared data.
            counter.value+=1
    
if __name__=="__main__":
    counter=Value('i',0) #Creates a shared integer initialized to 0.
    processes=[Process(target=increment,args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(counter.value) #The syntax used to read or write the actual data.