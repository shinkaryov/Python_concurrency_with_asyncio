from asyncio import Future
import asyncio


def make_request():
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')


async def main():
    future = make_request()
    print(f'Is the future done? {future.done()}')
    value = await future
    print(f'Is the future done? {future.done()}')
    print(f'Future returned: {value}')

asyncio.run(main())

