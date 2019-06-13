
class XString(object):
    def is_p(s):
        """ is palindrome
        type s: string
        rtype : boolean
        """
        if len(s) <= 1:
            return True
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def lcs(self, word1, word2):
        """ longest common substring
        :type word1: str
        :type word2: str
        :rtype: int
        :return the length of longest common substring, e.g, m('1a2b3c4d', 'a5b6c777d88') return 4 (length of 'abcd')
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: return 0

        dp = [0] * n
        res = 0
        for i, a in enumerate(word1):
        	cur_max = 1
        	for j, b in enumerate(word2):
        		aux = dp[j]
        		if a == b: dp[j] = cur_max
        		if aux + 1 > cur_max: cur_max = aux + 1
        		res = max(res, dp[j])
        return res 


# for Strings
# decide whether list(s) in list(t). e.g., is_sub('abc', 'akbkck') == True
def is_substring(s, t):
    it = iter(t)
    return all(c in it for c in s)


class PriorityQueue(object): 
    def __init__(self, li=[]): 
        self.queue = [] 
        for i in li:
            self.push(i)
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for return the size of queue 
    def size(self):
        return len(self.queue)

    # for inserting an element in the queue 
    def push(self, data):
        insert_idx = bisect_left(self.queue, data)
        self.queue.insert(insert_idx, data)

    # for popping an element based on Priority 
    def pop(self): 
        return self.queue.pop()


# # from bisect import bisect_left

# pq = PriorityQueue()
# for i in [2, 5, 4, 3, 9, 6]:
#     pq.push(i)

# while not pq.isEmpty():
#     print(pq.pop())

# same as from itertools import permutations
def perms(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    print(cycles)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

