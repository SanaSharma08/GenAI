# Multiprocess with Queue and Value

# using multiprocessing : more efficient than multithreading

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some number...")
    total=0
    for i in range(10**9):
        total+=i
    print("Done ✅")
    
if __name__ == "__main__":
    start=time.time()
    Processes=[Process(target=cpu_heavy) for _ in range(5)]

    [t.start() for t in Processes]
    [t.join() for t in Processes]

    end=time.time()
    print(f"Time taken: {end-start:.2f} seconds")