import asyncio
from functools import wraps
from time import perf_counter


async def take_coroutine_type():
    await asyncio.sleep(1)


def measure_time(func):
    if type(func) is type(lambda: None):
        @wraps(func)
        def main_func(*args, **kwargs):
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            print(f'Длительность функции {func.__name__} = {end_time - start_time:0.9f}')
            return result
        return main_func
    elif type(func) is type(take_coroutine_type()):
        @wraps(func)
        async def main_coroutine(*args, **kwargs):
            start_time = perf_counter()
            result = await func(*args, **kwargs)
            end_time = perf_counter()
            print(f'Длительность асинхронной функции {func.__name__} = {end_time - start_time:0.9f}')
            return result
        return main_coroutine


@measure_time
def sync():
    pass


@measure_time
async def my_coroutine():
    await asyncio.sleep(2)


if __name__=='__main__':
    sync()
    asyncio.run(my_coroutine())
