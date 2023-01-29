from reusable.util import delay
import asyncio


async def add_one(number: int) -> int:
    print(f'Adding one to {number}')
    return number + 1


async def hello_world_message() -> None:
    await delay(1)
    print('Hello World!')


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(f'one_plus_one is {one_plus_one}')
    print(f'message is {message}')

asyncio.run(main())
