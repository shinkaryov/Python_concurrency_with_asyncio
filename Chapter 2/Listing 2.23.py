import asyncio
from reusable.util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    return sum(i * i for i in range(10_000_000))


async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main(), debug=True)
