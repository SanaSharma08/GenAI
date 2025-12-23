import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2) 
    #You can only use await inside an async function.
    print(f" {name} is ready...")
    
 
async def main():
    await asyncio.gather(
        # Multiple co-routines gathered with gather() and will be scheduled in event queue
        brew("Masala Chai"),
        brew("Masala Chai"),
        brew("Masala Chai"),
    )
asyncio.run(main())