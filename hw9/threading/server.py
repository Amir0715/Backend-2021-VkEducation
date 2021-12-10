import argparse
import socketserver
import threading
import logging
from typing import Counter
import requests
import json


class ThreadedRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()  # получаем данные
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: {self.client_address} send {data}")
        json = self.worker(data)
        # отправляем данные
        self.wfile.write(bytes(str(json), 'UTF-8'))

    def worker(self, url):
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread waiting!")
        with self.server.sem:
            self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread join!")
            res = self.top_k(url)
            d = {}
            for k, v in res:
                d[k] = v
            d = json.dumps(d)
            self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread left!")
            return d

    def top_k(self, url):
        data = requests.get(url)
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: [{url}]: {data}")
        return Counter(data.text).most_common(self.server.k)


class Master(socketserver.ThreadingTCPServer):
    sem = None
    logger: logging.Logger = logging.getLogger("server")
    allow_reuse_address = True
    k = 0

    def __init__(self, host: str, port: int, handler_classRequestHandler: socketserver.BaseRequestHandler, worker_limit: int, k: int):
        super().__init__((host, port), handler_classRequestHandler)

        self.sem = threading.Semaphore(worker_limit)
        self.k = k

        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('server.log', mode='w')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(fh)
        debug_str = f'Create server instanse with host {host}, port {port}'
        self.logger.debug(debug_str)

        print(debug_str)

    def _get_statistic(self):
        pass


def run():
    with Master(*address, ThreadedRequestHandler, 7) as m:
        m.serve_forever()


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workers', type=int, default=1)
    parser.add_argument('-k', '--top_k', type=int, default=7)
    parser.add_argument('-p', '--port', type=int, default=8000)
    return parser


if __name__ == '__main__':
    namespace = createParser().parse_args()
    address = ('localhost', namespace.port)
    with Master(*address, ThreadedRequestHandler, namespace.workers, namespace.top_k) as m:
        m.serve_forever()
