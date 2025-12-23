# What is Global Interpreter Lock - GIL


#GIL in action
# this shows gil with multithreading
import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count=0 # bot threads will try to access this variable's memory, and mutex will come into picture that is why it will take longer as threads grow as final op will only be printed after all threads have finished execution.
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing...")
    
thread1=threading.Thread(target=brew_chai,name="Barista-1")
thread2=threading.Thread(target=brew_chai,name="Barista-2")

start=time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end=time.time()

print(f"total time taken: {end-start:.2f} seconds")