from rq import Worker, Queue, Connection
from redis import Redis


queue_name = 'test_queue'
redis_client = Redis(host='localhost', port=6379, db=0)
queue = Queue(queue_name, connection=redis_client)


with Connection(redis_client):
    # Run workers with the specified number
    worker_count = 2  # Change this to the desired number of workers

    # Create worker instances
    workers = [Worker(queue_name, connection=redis_client) for _ in range(worker_count)]

    # Start the workers
    worker_threads = [worker.work() for worker in workers]

    # Wait for all workers to finish
    for worker_thread in worker_threads:
        worker_thread.join()