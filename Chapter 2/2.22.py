import asyncio
from reusable.util import delay


def call_later():
    print("I'm being called later")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_later(1, call_later)
    await delay(2)

asyncio.run(main())
