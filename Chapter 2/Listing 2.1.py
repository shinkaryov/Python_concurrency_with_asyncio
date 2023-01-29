import asyncio
import time


def print_hello_world():
    print("Hello World!")


async def my_coroutine() -> None:
    print("Hello World!")

time_start = time.time()
asyncio.run(my_coroutine())
time_end = time.time()
print(f"Total time taken: {time_end - time_start}")

time_start = time.time()
print_hello_world()
time_end = time.time()
print(f"Total time taken: {time_end - time_start}")

