from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
import threading, time
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007



# https://leetcode.com/problems/design-bounded-blocking-queue/description/
# Medium
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.lock = threading.Semaphore(capacity) 
        self.capacity = capacity 
        self.queue = deque()

    def enqueue(self, element: int) -> None:
        with self.lock:
            self.queue.append(element)

    def dequeue(self) -> int:
        while not self.queue:
            time.sleep(0.1)
        return self.queue.popleft()


    def size(self) -> int:
        return len(self.queue)
        
