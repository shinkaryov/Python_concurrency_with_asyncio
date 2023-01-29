import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'


async def main() -> None:
    hello_world = await hello_world_message()
    print(hello_world)

asyncio.run(main())