# Managing Process with queues.
# More efficient than regular multiprocessing
#This code demonstrates Inter-Process Communication (IPC) using a Queue.

from multiprocessing import Process,Queue, Value

def prepare_chai(queue):
    #Inside the child process, we "drop" the string into the queue
    queue.put("Masala chai is ready!") #Sends data into the channel (from the worker).
    
counter=Value('i',0)
    
if __name__=="__main__":
    queue=Queue() # object creation
    #Creates the shared communication channel.

    p=Process(target=prepare_chai,args=(queue,))

    p.start()
    p.join()
    
    #In the main process, we "pull" the string out. If the queue were empty, get() would wait (block) until something appeared.
    print(queue.get()) #Retrieves data from the channel (in the main process).