import threading
import queue
import concurrent.futures
import random
import logging
import time
import vessel_math as vm


def cam_cap(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(10, 99)
        logging.info("captured: %s", message)
        queue.put(message, "Camera")

def alg_store(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("stored: %s",message)
        

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    patient_instance = vm.Vessel_math("DavidsonLiam")
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(cam_cap, pipeline, event)
        executor.submit(alg_store, pipeline, event)


        time.sleep(.2)
        event.set()