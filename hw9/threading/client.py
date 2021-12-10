from queue import Queue
import socket
import threading
import argparse
import logging


class Client:
    urls = Queue()
    logger: logging.Logger = logging.getLogger("client")

    def __init__(self, address, filepath, thread_count) -> None:
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('client.log', mode='w')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(fh)

        self.address = address
        self.read_file(filepath)

        self.logger.debug(f'[{threading.current_thread().getName()}] Client instance has been created with [{address=}] [{filepath=}] [{thread_count=}]')

        self.threads = [
            threading.Thread(target=self.worker, args=(self.urls, ), daemon=True)
            for _ in range(thread_count)
        ]
        self.logger.debug(f'[{threading.current_thread().getName()}] {thread_count} threads has been created')

    def run(self):
        for th in self.threads:
            th.start()
            self.logger.debug(f'[{threading.current_thread().getName()}] {th.getName()} starting...')
        for th in self.threads:
            th.join()
            self.logger.debug(f'[{threading.current_thread().getName()}] {th.getName()} joining...')

    def read_file(self, filepath):
        with open(filepath) as f:
            urls = f.read().splitlines()
            for url in urls:
                self.urls.put(url)
            self.logger.debug(f"[{threading.current_thread().getName()}] {len(urls)} urls have been added")

    def worker(self, urls: Queue[str]):
        while True:
            url = urls.get()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.connect(self.address)
            self.logger.debug(f"[{threading.current_thread().name}]: connect to {self.address}!")

            sock.sendall(bytes(url+"\n", 'utf-8'))
            self.logger.debug(f"[{threading.current_thread().name}]: {url} have been sended!")

            rcv = str(sock.recv(1024), "utf-8")
            self.logger.debug(f"[{threading.current_thread().name}]: waiting responce")

            if rcv:
                self.logger.debug(f"[{threading.current_thread().name}]: {url} : {rcv}")
                print(f"{url}: {rcv}")
            sock.close()


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='urls')
    parser.add_argument('-t', '--threads', type=int, default=1)
    parser.add_argument('-p', '--port', type=int, default=8000)
    return parser


if __name__ == "__main__":
    namespace = createParser().parse_args()

    ADDRESS = "localhost", namespace.port
    client = Client(ADDRESS, namespace.file, namespace.threads)
    client.run()
