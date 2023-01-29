from asyncio import Future

my_future = Future()

print(f'Is my future done? {my_future.done()}')

my_future.set_result('Hello from the future!')

print(f'Is my future done? {my_future.done()}')
print(f'What is my future result? {my_future.result()}')
