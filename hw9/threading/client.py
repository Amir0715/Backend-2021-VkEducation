from queue import Queue
import socket
import threading


class Client:
    urls = Queue()

    def __init__(self, address, filepath, thread_count) -> None:
        self.address = address
        self.read_file(filepath)
        self.threads = [
            threading.Thread(target=self.worker, args=(self.urls, ), daemon=True)
            for _ in range(thread_count)
        ]

    def run(self):
        for th in self.threads:
            th.start()
        for th in self.threads:
            th.join()

    def read_file(self, filepath):
        with open(filepath) as f:
            urls = f.read().splitlines()
            for url in urls:
                self.urls.put(url)
            print(f"{len(urls)} urls have been added")

    def worker(self, urls: Queue[str]):
        while True:
            url = urls.get()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.connect(self.address)
            print(f"[{threading.current_thread().name}]: connect to {self.address}!")

            sock.sendall(bytes(url+"\n", 'utf-8'))
            print(f"[{threading.current_thread().name}]: {url} have been sended!")

            rcv = str(sock.recv(1024), "utf-8")
            print(f"[{threading.current_thread().name}]: waiting responce")

            if rcv:
                print(f"[{threading.current_thread().name}]: {url} : {rcv}")

            sock.close()


if __name__ == "__main__":
    ADDRESS = "localhost", 8000
    client = Client(ADDRESS, 'urls', 7)
    client.run()
