import queue
import random
import uuid
from time import sleep

q = queue.Queue()
counter = 0


def generate_request():
    global counter
    counter += 1
    randomiser = random.random()
    message = str()
    if randomiser > 0.5:
        message = f"id: {counter}, payload: {uuid.uuid4()}"
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
