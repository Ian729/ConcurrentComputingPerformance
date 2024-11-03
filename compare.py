import requests
import time
import threading
import multiprocessing
import asyncio
import aiohttp

URL = 'http://127.0.0.1:5000/api/data'
NUM_REQUESTS = 10


# thread
def thread_request():
    response = requests.get(URL)
    print(response.json())


def test_multithreading():
    threads = []
    start_time = time.time()

    for _ in range(NUM_REQUESTS):
        thread = threading.Thread(target=thread_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Time taken with threading: {time.time() - start_time} seconds')


# process
def process_request():
    response = requests.get(URL)
    print(response.json())


def test_multiprocessing():
    processes = []
    start_time = time.time()

    for _ in range(NUM_REQUESTS):
        process = multiprocessing.Process(target=process_request)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Time taken with multiprocessing: {time.time() - start_time} seconds')

# coroutine
async def async_request(session):
    async with session.get(URL) as response:
        print(await response.json())


async def test_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session) for _ in range(NUM_REQUESTS)]
        start_time = time.time()
        await asyncio.gather(*tasks)
        print(f'Time taken with asyncio: {time.time() - start_time} seconds')


if __name__ == '__main__':
    test_multithreading()
    test_multiprocessing()
    asyncio.run(test_asyncio())
