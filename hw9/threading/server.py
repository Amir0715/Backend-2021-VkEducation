import socketserver
import threading
import typing
import queue
import logging

from worker import Worker


class ThreadedRequestHandler(socketserver.StreamRequestHandler):
    # logger: logging.Logger = logging.getLogger("StreamRequestHandler")

    # def setup(self) -> None:
    #     self.logger.setLevel(logging.DEBUG)
    #     fh = logging.FileHandler('requests.log')
    #     fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    #     self.logger.addHandler(fh)
    #     # self.logger.debug(f'Request setup')
    #     return super().setup()

    def handle(self):
        self.data = self.rfile.readline().strip()
        self.server.urls.put(self.data)
        print(f"{self.data}, len(urls) = {self.server.urls.qsize()}")
        self.wfile.write(self.data)

# TODO: Отнаследоваться от socketserver.ThreadingTCPServer,
# что бы можно было получить доступ к полям мастера через объект 
# self.server в RequestHandler классе


class Master(socketserver.ThreadingTCPServer):
    urls: queue.Queue[str] = queue.Queue()
    workers: list[threading.Thread] = []
    logger: logging.Logger = logging.getLogger("server")

    def __init__(self, host: str, port: int, handler_classRequestHandler: socketserver.BaseRequestHandler, worker_count: int):
        super().__init__((host, port), handler_classRequestHandler)

        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('server.log')
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(fh)
        debug_str = f'Create server instanse with host {host}, port {port}'
        self.logger.debug(debug_str)

        print(debug_str)
        self._create_workers(worker_count)

    def _get_statistic(self):
        pass

    def _create_workers(self, worker_count: int):
        for i in range(worker_count):
            worker = Worker(self.urls)
            # thread = threading.Thread(Worker.run)

def run():
    with Master(*address, ThreadedRequestHandler, 7) as m:
        m.serve_forever()
    


if __name__ == '__main__':
    address = ('localhost', 8000)
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()
