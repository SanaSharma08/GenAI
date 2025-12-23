#Locks
import threading

counter=0
lock = threading.Lock() #object acts like a "talking stick" or a physical key to a room.

def increament():
    global counter
    for _ in range(100000):
        with lock:
            #This is a context manager. When a thread enters this block, it "acquires" the lock. If another thread tries to enter a with lock: block at the same time, it is forced to wait (it blocks) until the first thread is finished.
            counter+=1
        #Once the code inside the with block finishes, the lock is automatically released, allowing the next waiting thread to proceed.

threads = [threading.Thread(target=increament) for _ in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")
#Because of the lock, the output will consistently be Final counter: 1000000. If you removed the with lock: line, the final number "could" be lower and different every time you ran the script.