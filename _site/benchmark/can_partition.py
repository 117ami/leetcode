import random
import time
 
def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__.upper(),
                         time=runtime))
        return value
    return function_timer
 
def isodd(n):
	return n % 2 > 0

def find_patition_dp(nums):
    mus, n = sum(nums), len(nums)
    if isodd(mus): return False 

    target = mus // 2
    part = [[True for i in range(n + 1)] for j in range(target + 1)]

    for i in range(n + 1): part[0][i] = True
    for i in range(1, target + 1): part[i][0] = False

    for i in range(1, target + 1):
        for j in range(n + 1):
            part[i][j] = part[i][j-1]
            if i >= nums[j-1]:
                part[i][j] = part[i][j] or part[i - arr[j-1]][j-1]

    return part[target][n]

def find_patition(nums):
    mus = sum(nums)
    if isodd(mus): return False

    target = mus // 2
    visited = {}

    def rec(i, acc):
        if acc == target: return True
        if i >= len(nums) or acc > target: return False
        key = "{}-{}".format(acc, i)
        if key in visited: return visited[key]

        r = rec(i + 1, acc + nums[i]) or rec(i + 1, acc)
        visited[key] = r 
        return r

    return rec(0, 0)


@timerfunc
def dpmethod():
	for i in range(100):
		nums = [random.randint(1, 3) for _ in range(300)]
		find_patition_dp(nums)


@timerfunc
def recmethod():
	for i in range(100):
		nums = [random.randint(1, 3) for _ in range(300)]
		find_patition(nums)


if __name__ == '__main__':
	dpmethod()
	recmethod()

