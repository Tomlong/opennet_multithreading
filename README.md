## Description

This is the assignment 1 which is about multithreading application for the OpenNet

## Structure
- `main.py`: the main application, which contains the producer and consumer threads.
    - `producer`: the producer thread which produce the message to the queue in `PRODUCER_INTERVAL_TIME` and would not append the message to the queue if the queue is full.
    - `consumer`: the consumer thread which consume the message from the queue in `CONSUMER_INTERVAL_TIME`

## Run local
1. Prepare the `.env` based on `.env.sample`
    ```bash
    PRODUCER_INTERVAL_TIME=0.1
    CONSUMER_INTERVAL_TIME=0.15
    MAX_QUEUE_SIZE=10
    ```
2. poetry install
3. run main.py
    ```bash
    poetry run python main.py
    ```

### Run on docker
1. Adjust the environment variables in `docker-compose.yml` if necessary.
    - The env default values are as following.
        ```bash
        PRODUCER_INTERVAL_TIME=0.1
        CONSUMER_INTERVAL_TIME=0.15
        MAX_QUEUE_SIZE=10
        ```
2. build
    ```bash
    docker-compose build
    ```
3. run
    ```bash
    docker-compose run
    ```
