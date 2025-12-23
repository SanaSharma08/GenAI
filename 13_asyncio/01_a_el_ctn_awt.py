#Asyncio, Event loop, coroutines and await in python
import asyncio

async def brew_chai(): # Coroutine
    print("Brewing Chai...")
    await asyncio.sleep(2)
    print("Chai is ready!")
    
asyncio.run(brew_chai())