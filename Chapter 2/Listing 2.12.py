import asyncio
from reusable.util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(f'Result: {result}')
    except asyncio.exceptions.TimeoutError:
        print('Timeout occurred')
        print(f'Was the task cancelled? {delay_task.cancelled()}')

asyncio.run(main())
