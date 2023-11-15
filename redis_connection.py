from redis import Redis
from rq import Queue


redis_client = Redis(host='localhost', port=6379, db=0)

# redis_client.lpush('my_queue', 'item1')
# redis_client.lpush('my_queue', 'item2')
# redis_client.lpush('my_queue', 'item3')

# length = redis_client.llen('my_queue')
# print(f"Queue Length: {length}")

# item = redis_client.rpop('my_queue')
# print(F"Dequeued Item: {item.decode('utf-8')}")

# length = redis_client.llen('my_queue')
# print(f"Queue Length: {length}")


# queue = Queue('test_queue', connection=redis_client)
# # queue.delete()

# # job = queue.enqueue(get_solution_matrix, 3, 6)
# job = queue.enqueue('no_prune.main.srgan',
#                         '6_no_prune_2023-11-09 15:27:44.065722.png',
#                         'localhost',
#                         "2023-11-09T14:23:19.463046"
#                     )

# print(job.get_id())
# # job = queue.fetch_job('9fbef7fd-c3b1-43ee-b3af-da239f3881ee')
# # print(job.result)