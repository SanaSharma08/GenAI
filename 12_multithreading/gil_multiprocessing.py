# This shows gil with multiprocessing
# You can actually bypass gil in parallelism.
# comparatively faster than multithreading.
#If you ran this same logic using threading, the time taken would likely be the sum of both counts (e.g., 10 seconds). With multiprocessing, the time taken is only as long as the slowest single process (e.g., 5 seconds), because they occur at the same time.

#This code is a classic demonstration of how Python handles CPU-bound tasks (tasks that require heavy calculation) using the multiprocessing module.

#The core idea here is that while Python's Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecode at the same time, multiprocessing sidesteps this by giving each task its own entire Python interpreter and memory space.

#In standard Python (CPython), the GIL acts like a "one-way bridge" where only one thread can cross (execute) at a time. This makes multithreading slow for heavy math.

#Multiprocessing works differently:
# Instead of one process with multiple threads, it creates multiple independent processes.
# Each process has its own GIL.
# Since they are separate processes, the Operating System can schedule them to run on different CPU cores simultaneously.

from multiprocessing import Process
import time

#In a multithreaded environment, the GIL would make these two processes wait for each other. In multiprocessing, they run in parallel.
def crunch_number():
    print(f"Started the count process....")
    count=0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")
    
# We are bypassing gil so we need to specify an entry point to the code. The if __name__=="__main__": block does exactly that.


if __name__=="__main__": #"Only execute the following code if I am the boss (the original script). If I am a worker process just being imported, stay quiet and wait for instructions."
    #This is crucial in multiprocessing. When you start a new Process, Python "imports" your script again in that new process.
    #Without this if block, the new process would start its own sub-processes, creating an infinite loop of process creation (a "process bomb") that would crash your computer.
    #This block ensures the code only runs once in the main process.
    start=time.time()

    p1=Process(target=crunch_number)
    p2=Process(target=crunch_number)

    p1.start() #p1.start(): This tells the OS to spawn the new process and begin executing crunch_number.
    p2.start()

    p1.join() #This is a "wait" command. The main script will stop at this line and wait for p1 to finish before moving on to calculate the total time.
    p2.join()

    end=time.time()

    print(f"Total time with multiprocessing is {end-start:.2f} seconds")

