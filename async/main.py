import asyncio
from time import sleep

async def task(i):
    print(f'Starting task {i}')
    await asyncio.sleep(2)
    print(f'Doing task {i}')



async def main():
    t1 = task(1)
    t2 = task(2)
    t3 = task(3)
    t4 = task(4)

    t1_t = asyncio.create_task(t1)
    t2_t = asyncio.create_task(t2)
    await t3
    await t4
    await t1_t
    await t2_t


if __name__ == '__main__':
    coro = main()
    print(coro)
    asyncio.run(coro)

