import os
import threading
import time

from collections import deque
from random import randint
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
MAX_QUEUE_SIZE = 10
queue = deque(maxlen=10)
stop_event = threading.Event()

PRODUCER_INTERVAL_TIME = float(os.getenv('PRODUCER_INTERVAL_TIME', 0.1))
CONSUMER_INTERVAL_TIME = float(os.getenv('CONSUMER_INTERVAL_TIME', 0.15))
EXECUTE_TIME = float(os.getenv('EXECUTE_TIME', 10))


def producer():
    while not stop_event.is_set():
        if len(queue) < MAX_QUEUE_SIZE:
            item = randint(1, 100)
            queue.append(item)
            logger.info(f'produce msg: {item}')
        else:
            logger.info('queue is full')
        time.sleep(PRODUCER_INTERVAL_TIME)


def consumer():
    while not stop_event.is_set():
        logger.info(f'queue: {queue}')
        if queue:
            item = queue.popleft()
            logger.info(f'consume msg: {item}')
        time.sleep(CONSUMER_INTERVAL_TIME)
    logger.info('consumer: done')


def main():

    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()
    time.sleep(EXECUTE_TIME)
    stop_event.set()

    thread_producer.join()
    thread_consumer.join()


if __name__ == "__main__":
    main()
