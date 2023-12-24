import queue
import random
from time import sleep

q = queue.Queue()


def generate_request():
    id = random.random()
    message = str()
    if id > 0.5:
        message = f"Id: {str(id).lstrip('0.')}"
        q.put(message)
    sleep(0.2)


def process_request() -> str:
    res = str()
    if q.empty():
        res = "Queue is empty"
    else:
        res = q.get()
        sleep(0.2)
    return print(res)


def __main__():
    print("Press Ctrl+C to exit")
    while True:
        try:
            generate_request()
            process_request()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    __main__()
