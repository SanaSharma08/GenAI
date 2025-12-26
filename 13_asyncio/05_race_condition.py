import threading

chai_stock=0

def restock():
    global chai_stock
    for _ in range(100_000):
        chai_stock +=1
        
threads=[threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock)
#very unpredictable - may or may not happen
# might get 200000 mostly but maybe be 19999  or less due to race condition where a thread might read a value before another can write resulting in some writing getting missed.
