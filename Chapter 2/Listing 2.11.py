import asyncio
from asyncio import CancelledError
from reusable.util import delay


async def main():
    long_running_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_running_task.done():
        print(f'{seconds_elapsed} seconds elapsed')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_running_task.cancel()

    try:
        await long_running_task
    except CancelledError:
        print('Task cancelled')

asyncio.run(main())
