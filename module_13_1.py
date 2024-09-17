import asyncio


async def start_strongman(name, power):
    current_ball = 0
    amount_of_balls = 5
    print(f'Силач {name} начал соревнования')
    while current_ball != amount_of_balls:
        await asyncio.sleep(amount_of_balls - power)
        print(f'Силач {name} поднял  шар номер {current_ball + 1}')
        current_ball += 1
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Victor', 3))
    task_2 = asyncio.create_task(start_strongman('Jamal', 4))
    task_3 = asyncio.create_task(start_strongman('Vlad', 25))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
