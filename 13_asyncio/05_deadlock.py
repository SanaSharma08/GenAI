import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acquired Lock A")
        # Sleep to give Task 2 time to grab Lock B
        time.sleep(1) 
        print("Task 1 trying to acquire Lock B...")
        with lock_b:
            print("Task 1 acquired Lock B")

def task2():
    with lock_b:
        print("Task 2 acquired Lock B")
        # Sleep to give Task 1 time to grab Lock A
        time.sleep(1) 
        print("Task 2 trying to acquire Lock A...")
        with lock_a:
            print("Task 2 acquired Lock A")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
print("Main program finished") # This line will NEVER be printed


# Task 1 grabs Lock A and sleeps.

# Task 2 grabs Lock B and sleeps.

# Task 1 wakes up and tries to grab Lock B (held by Task 2). It waits.

# Task 2 wakes up and tries to grab Lock A (held by Task 1). It waits.

# The program hangs forever. You will have to manually stop it (usually Ctrl + C or hitting the Stop button in your IDE).