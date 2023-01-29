import os
import threading

print(f'Python process running with process id: {os.getpid()}')
total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'Python is currently running {total_threads} threads')
print(f'This thread is named: {thread_name}')
