# requirement python 3.7.1
import asyncio

def inner_proc(lst):
    print(lst)


async def main():

    accounts = ['123', '124', '125', '126', '127', '128', '129', '130', '131', '132']  # etc
    n = 8 #кол-во shared_future
    futures = []
    if len(accounts) > 0:
        lst_lst = [accounts[i::n] for i in range(n)]
        for lst in lst_lst:
            #параллельный вызов метода со скриптом на каждой БД
            future = asyncio.create_task(inner_proc(lst))
            futures.append(future)
        # дожидаемся выполнения всех вызовов
        for future in futures:
            await future

asyncio.run(main())