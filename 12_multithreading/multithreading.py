# What is concurrency and parallelism
# threading

import threading
import time


# Task 1
def take_order():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2) # time delay
        
# Task 2     
def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3) # time
 
 
        
# creating threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

# Invoking threads
order_thread.start()
brew_thread.start()
# This is a multithreading example and you won't get your output untill both threads finish executing.

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taekn and chai brewed!")
