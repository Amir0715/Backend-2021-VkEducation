import socketserver
import threading
import typing
import queue
import logging

from worker import Worker


class ThreadedRequestHandler(socketserver.StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.readline().strip()
        self.server
        self.wfile.write(self.data)

# TODO: Отнаследоваться от socketserver.ThreadingTCPServer,
# что бы можно было получить доступ к полям мастера через объект 
# self.server в RequestHandler классе


class Master:
    urls: queue.Queue[str] = queue.Queue()
    workers: list[threading.Thread] = []
    server: socketserver.ThreadingTCPServer = None
    logger: logging.Logger = logging.getLogger("server")

    def __init__(self, host: str, port: int):
        self.server = socketserver.ThreadingTCPServer(
            (host, port), ThreadedRequestHandler)

        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler('server.log')
        fh.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(fh)
        self.logger.debug(
            f'Create server instanse with host {host} port {port}')

    def start(self, worker_count: int) -> socketserver.ThreadingTCPServer:
        '''Запускает сервер и воркеров и возвращает объект сервера
        '''
        self.logger.debug('Server loop running in thread: {}'.format(
            threading.current_thread().getName()))
        self.server.serve_forever()
        self._create_workers(worker_count)
        return self.server

    def _get_statistic(self):
        pass

    def _create_workers(self, worker_count: int):
        for i in range(worker_count):
            worker = Worker(self.urls)
            thread = threading.Thread(Worker.run)


if __name__ == '__main__':
    address = ('localhost', 8080)
    m = Master(*address)
    t = threading.Thread(target=m.start, args=(7, ))
    t.start()
    t.join()
