import redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)

# redis_client.lpush('my_queue', 'item1')
# redis_client.lpush('my_queue', 'item2')
# redis_client.lpush('my_queue', 'item3')

# length = redis_client.llen('my_queue')
# print(f"Queue Length: {length}")

# item = redis_client.rpop('my_queue')
# print(F"Dequeued Item: {item.decode('utf-8')}")

# length = redis_client.llen('my_queue')
# print(f"Queue Length: {length}")