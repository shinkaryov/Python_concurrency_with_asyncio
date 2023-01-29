import asyncio


async def coroutine_add_one(number) -> int:
    print(f'Adding one to {number}')
    return number + 1

result = asyncio.run(coroutine_add_one(5))

print(f'Coroutine result: {result}')