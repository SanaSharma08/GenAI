# Multiprocess with Queue and Value

# inefficient example with multithreading - we are comparing

import threading 
import time

def cpu_heavy():
    print(f"Crunching some number...")
    total=0
    for i in range(10**7):
        total+=i
    print("Done ✅")
    
start=time.time()
threads=[threading.Thread(target=cpu_heavy) for _ in range(5)]

[t.start() for t in threads]
[t.join() for t in threads]

end=time.time()
print(f"Time taken: {end-start:.2f} seconds")

# Not an efficient approach - multiprocessing is a better approach for cpu heavy processes