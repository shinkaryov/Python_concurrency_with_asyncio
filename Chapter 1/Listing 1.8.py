import time
import threading
import requests


def read_example() -> None:
    response = requests.get("https://www.example.com")
    print(response.status_code)


thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)

thread_start= time.time()

thread1.start()
thread2.start()

print('All threads started')

thread1.join()
thread2.join()

thread_end = time.time()

print(f'Total time taken: {thread_end - thread_start}')