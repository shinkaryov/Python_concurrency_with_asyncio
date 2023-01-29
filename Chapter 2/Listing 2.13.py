import asyncio
from reusable.util import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(f'Task completed with result: {result}')
    except asyncio.TimeoutError:
        print("Task took too long to complete")
        result = await task
        print(f'Task completed with result: {result}')

asyncio.run(main())

