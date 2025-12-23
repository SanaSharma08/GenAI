import threading
import time

def prepare_chai(type_,wait_time):
    print(f"{type_} chai : brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready!")
    
t1=threading.Thread(target=prepare_chai,args=("Masala",4))
t2=threading.Thread(target=prepare_chai,args=("Ginger",2))

start=time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end=time.time()
print(f"Order Complete in {end-start:.2f} seconds!")