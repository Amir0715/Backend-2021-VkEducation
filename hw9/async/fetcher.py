import argparse
import logging
from queue import Queue
import threading
from typing import Counter
import asyncio
import aiohttp

logging.basicConfig(filemode='w', filename='fetcher.log', level=logging.DEBUG)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='urls')
    parser.add_argument('-c', '--concurent', type=int, default=1)
    parser.add_argument('-k', '--top_k', type=int, default=10)
    return parser


def read_file(filepath):
    urls = []
    with open(filepath) as f:
        urls = f.read().splitlines()
        logging.debug(f"[{threading.current_thread().getName()}] {len(urls)} urls have been added")
    return urls


async def top_k(session, lock, url, k):
    async with lock:
        async with session.get(url) as resp:
            data = await resp.read()
            logging.debug(f"[{threading.current_thread().getName()}]: [{url}]: done")
            return Counter(data).most_common(k)


async def main():
    namespace = createParser().parse_args()
    urls = read_file(namespace.file)
    lock = asyncio.Semaphore(namespace.concurent)
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(top_k(session, lock, url, namespace.top_k))
            for url in urls
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
