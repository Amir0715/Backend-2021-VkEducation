import socketserver
import threading
import logging
from worker import Worker
import requests


class ThreadedRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()  # получаем данные
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: {self.client_address} send {data}")
        json = self.worker(data)
        # отправляем данные
        self.wfile.write(bytes(str(json.status_code)+'\n', 'UTF-8'))

    def worker(self, url):
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread waiting!")
        with self.server.sem:
            self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread join!")
            res = self.top_k(url)
            self.server.logger.debug(f"[{threading.current_thread().getName()}]: thread left!")
            return res

    def top_k(self, url):
        data = requests.get(url)
        self.server.logger.debug(f"[{threading.current_thread().getName()}]: [{url}]: {data}")
        return data


class Master(socketserver.ThreadingTCPServer):
    sem = None
    logger: logging.Logger = logging.getLogger("server")
    allow_reuse_address = True

    def __init__(self, host: str, port: int, handler_classRequestHandler: socketserver.BaseRequestHandler, worker_limit: int):
        super().__init__((host, port), handler_classRequestHandler)

        self.sem = threading.Semaphore(worker_limit)
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('server.log')
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


if __name__ == '__main__':
    address = ('localhost', 8000)
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()
