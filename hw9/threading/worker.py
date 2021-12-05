import queue
from socket import socket


class Worker:
    urls: queue.Queue[str] = None

    def __init__(self, urls: queue.Queue[str]):
        self.urls = urls

    def run(self):
        pass

    def fetch_url(self, url: str):
        pass

    def top_words(self, n: int):
        pass
