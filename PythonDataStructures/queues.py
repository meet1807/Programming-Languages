# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends

from collections import deque

queue = deque(["Hello", "meet", "patel"])
queue.append("world")  # added at the end of the queue
queue.popleft()        # removes the first element   #FIFO
