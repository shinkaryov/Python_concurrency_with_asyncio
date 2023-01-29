import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'Waiting {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'Finished waiting {delay_seconds} seconds')
    return delay_seconds
