import logging
import threading
import time
import concurrent.futures
import random
import queue



def producer(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(10, 99)
        logging.info("Producer got message: %s", message)
        queue.put(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s  (size=%s)", message, queue.qsize()
        )

    logging.info("Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(5)
        logging.info("Main: about to set event")
        event.set()