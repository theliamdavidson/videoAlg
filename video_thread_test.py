import threading
import queue
import concurrent.futures
import random
import logging
import vessel_math as vm

artery_num = 0
message_list = []
len_list = []

def cam_cap(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(10, 99)
        queue.put(message, "Camera")

def alg_store(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        if len(message_list) < 5:
            message_list.append(message)
        else:
            if len(len_list) == 50:
                event.set()
            logging.info("run through the ligorithm: %s",message_list)
            algThread = threading.Thread(target=patient_instance.converter, args=(message_list,))
            algThread.start()
            algThread.join()
            message_list.clear()
            len_list.append("i")
            message_list.append(len(len_list))
            
            

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    patient_instance = vm.Vessel_math("DavidsonLiam")
    message_list.append(len(len_list))
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(cam_cap, pipeline, event)
        executor.submit(alg_store, pipeline, event)

    logging.info("done")

    vessel_group_var = patient_instance.macro_vessel_calculations()

    print(vessel_group_var)