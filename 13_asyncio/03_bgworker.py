import asyncio
import threading
import time

def background_worker(): 
    # runs in the background for as much time as fetch_orders takes to execute.
    while True:
        time.sleep(1)
        print(f"logging the system health")
        
async def fetch_orders():
    await asyncio.sleep(3)
    print("order fetched")
    
    
threading.Thread(target=background_worker,daemon=True).start()
# we will learn more about daemon in 04

asyncio.run(fetch_orders())