import asyncio
from time import sleep
import random

async def my_coroutine()->int:
    print("Coroutine started")
    await asyncio.sleep(5)
    print("Coroutine ended")
    value: int = random.randint(-10, 10)
    print(f"Random value: {value}")
    return value

async def my_coroutine(sleep: int)->int:
    print("Coroutine started")
    await asyncio.sleep(sleep)
    print("Coroutine ended")
    value: int = random.randint(-10, 10)
    print(f"Random value: {value}")
    return value

async def main_without_arguments():
    random_values = await asyncio.gather(my_coroutine(), my_coroutine(), my_coroutine())
    return sum(random_values)
    
async def main_with_arguments():
    random_values = await asyncio.gather(my_coroutine(2), my_coroutine(5), my_coroutine(1))
    return sum(random_values)

if __name__ == "__main__":
    #print(type(my_coroutine())) # prints <class 'coroutine'>
    # Simple coroutine
    #asyncio.run(my_coroutine())
    
    # Gather coroutines
    #print(f"The sum of the random values is {asyncio.run(main_without_arguments())}")
    
    # Coroutines with arguments
     print(f"The sum of the random values is {asyncio.run(main_with_arguments())}")