from random import randint
import random
import collections


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

    def lcslen(self, word1, word2):
        """ longest common substring
        :type word1: str
        :type word2: str
        :rtype: int
        :return the length of longest common substring, e.g, m('1a2b3c4d', 'a5b6c777d88') return 4 (length of 'abcd')
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return 0

        dp = [0] * n
        res = 0
        for i, a in enumerate(word1):
            cur_max = 1
            for j, b in enumerate(word2):
                aux = dp[j]
                if a == b:
                    dp[j] = cur_max
                if aux + 1 > cur_max:
                    cur_max = aux + 1
                res = max(res, dp[j])
        return res

    def lcs(self, s, t):
        """ return the longest common substring
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, idx = m, n, dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res[idx - 1] = s[i - 1]
                idx -= 1
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(res)

    def scs(self, s, t):
        # return shortest common super-sequence
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, idx = m, n, m + n - dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res[idx - 1], i, j = s[i - 1], i - 1, j - 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                res[idx - 1], i = s[i - 1], i - 1
            else:
                res[idx - 1], j = t[j - 1], j - 1
            idx -= 1

        if j > 0:
            i, s = j, t

        while i > 0:
            res[idx - 1], idx, i = s[i - 1], idx - 1, i - 1

        return ''.join(res)


# for Strings
# decide whether list(s) in list(t). e.g., is_sub('abc', 'akbkck') == True
def is_substring(s, t):
    it = iter(t)
    return all(c in it for c in s)


def is_letter(c):
    return c.isalpha()


def isodd(n):
    return n % 2 > 0


def iseven(n):
    return n % 2 == 0


"""decide nums, a list containing only positive integers, can be partitioned
into two equal subsets. Two methods:

1. recursion, time complexity, 2^n in worst case, can cause "maximum recursion depth exceeded in comparison" when n is large,
but usually, this method is VERY FAST.

2. dynamic programming. O(sum * n) (both time and space)
Not feasible for ARRAYS WITH BIG SUM.

Benchmark: [random(1, 100) x 100] x 5 times.  i.e., 5 rounds x size 100 x domain 1-100
rec 0.025 second / dp 5.04 seconds

[random(1, 100) x 200] x 5 times.
rec 0.04 second / dp 20.22 seconds
"""

# recursion method


def find_patition(nums):
    mus = sum(nums)
    if isodd(mus):
        return False

    target = mus // 2
    visited = {}

    def rec(i, acc):
        if acc == target:
            return True
        if i >= len(nums) or acc > target:
            return False
        key = "{}-{}".format(acc, i)
        if key in visited:
            return visited[key]

        r = rec(i + 1, acc + nums[i]) or rec(i + 1, acc)
        visited[key] = r
        return r

    return rec(0, 0)


# DP method
def find_patition_dp(nums):
    mus, n = sum(nums), len(nums)
    if isodd(mus):
        return False

    target = mus // 2
    part = [[True for i in range(n + 1)] for j in range(target + 1)]

    for i in range(n + 1):
        part[0][i] = True
    for i in range(1, target + 1):
        part[i][0] = False

    for i in range(1, target + 1):
        for j in range(n + 1):
            part[i][j] = part[i][j - 1]
            if i >= nums[j - 1]:
                part[i][j] = part[i][j] or part[i - arr[j - 1]][j - 1]

    return part[target][n]


def sort_by_last(arr):
    arr.sort(key=lambda x: x[-1])

# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.


def is_rectangle_overlap(a, b):
    if a[0] > b[0]:
        return is_rectangle_overlap(b, a)
    return not (a[2] <= b[0] or a[3] <= b[1] or a[1] >= b[3])


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

# Generates the next permutation lexicographically after a given permutation.
# It changes the given permutation in-place.


def next_permutation(arr):
    # Find the highest index i such that s[i] < s[i+1].
    # If no such index exists, the permutation is the last permutation.
    i = len(arr) - 1
    while i > 0:
        if arr[i] > arr[i - 1]:
            break
        i -= 1
    if i == 0:
        return []
    i -= 1

    # Find the highest index j > i such that s[j] > s[i]. Such a j must exist,
    # since i+1 is such an index.
    for j in reversed(range(i + 1, len(arr))):
        if arr[j] > arr[i]:
            break

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_from_list(lis):
    if len(lis) == 0:
        return None
    root = TreeNode(lis[0])
    st = [root]
    i, j = 0, 1
    while j < len(lis):
        r = st[i]
        i += 1
        if r is None:
            j += 1
        else:
            lv = lis[j]
            r.left = TreeNode(lv) if lv else None
            st.append(r.left)

            if j + 1 >= len(lis):
                break

            rv = lis[j + 1]
            r.right = TreeNode(rv) if rv else None
            st.append(r.right)

            j += 2

    return root


def arr2linkedlist(arr):
    if len(arr) == 0:
        return
    head = ListNode(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


def linkedlist2arr(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


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

    def lcslen(self, word1, word2):
        """ longest common substring
        :type word1: str
        :type word2: str
        :rtype: int
        :return the length of longest common substring, e.g, m('1a2b3c4d', 'a5b6c777d88') return 4 (length of 'abcd')
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return 0

        dp = [0] * n
        res = 0
        for i, a in enumerate(word1):
            cur_max = 1
            for j, b in enumerate(word2):
                aux = dp[j]
                if a == b:
                    dp[j] = cur_max
                if aux + 1 > cur_max:
                    cur_max = aux + 1
                res = max(res, dp[j])
        return res

    def lcs(self, s, t):
        """ return the longest common substring
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, idx = m, n, dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res[idx - 1] = s[i - 1]
                idx -= 1
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(res)

    def scs(self, s, t):
        # return shortest common super-sequence
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j, idx = m, n, m + n - dp[-1][-1]
        res = ['#'] * idx

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                res[idx - 1], i, j = s[i - 1], i - 1, j - 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                res[idx - 1], i = s[i - 1], i - 1
            else:
                res[idx - 1], j = t[j - 1], j - 1
            idx -= 1

        if j > 0:
            i, s = j, t

        while i > 0:
            res[idx - 1], idx, i = s[i - 1], idx - 1, i - 1

        return ''.join(res)


# for Strings
# decide whether list(s) in list(t). e.g., is_sub('abc', 'akbkck') == True
def is_substring(s, t):
    it = iter(t)
    return all(c in it for c in s)


def is_letter(c):
    return c.isalpha()


def isodd(n):
    return n % 2 > 0


def iseven(n):
    return n % 2 == 0


"""decide nums, a list containing only positive integers, can be partitioned
into two equal subsets. Two methods:

1. recursion, time complexity, 2^n in worst case, can cause "maximum recursion depth exceeded in comparison" when n is large,
but usually, this method is VERY FAST.

2. dynamic programming. O(sum * n) (both time and space)
Not feasible for ARRAYS WITH BIG SUM.

Benchmark: [random(1, 100) x 100] x 5 times.  i.e., 5 rounds x size 100 x domain 1-100
rec 0.025 second / dp 5.04 seconds

[random(1, 100) x 200] x 5 times.
rec 0.04 second / dp 20.22 seconds
"""

# recursion method


def find_patition(nums):
    mus = sum(nums)
    if isodd(mus):
        return False

    target = mus // 2
    visited = {}

    def rec(i, acc):
        if acc == target:
            return True
        if i >= len(nums) or acc > target:
            return False
        key = "{}-{}".format(acc, i)
        if key in visited:
            return visited[key]

        r = rec(i + 1, acc + nums[i]) or rec(i + 1, acc)
        visited[key] = r
        return r

    return rec(0, 0)


# DP method
def find_patition_dp(nums):
    mus, n = sum(nums), len(nums)
    if isodd(mus):
        return False

    target = mus // 2
    part = [[True for i in range(n + 1)] for j in range(target + 1)]

    for i in range(n + 1):
        part[0][i] = True
    for i in range(1, target + 1):
        part[i][0] = False

    for i in range(1, target + 1):
        for j in range(n + 1):
            part[i][j] = part[i][j - 1]
            if i >= nums[j - 1]:
                part[i][j] = part[i][j] or part[i - arr[j - 1]][j - 1]

    return part[target][n]


def sort_by_last(arr):
    arr.sort(key=lambda x: x[-1])

# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.


def is_rectangle_overlap(a, b):
    if a[0] > b[0]:
        return is_rectangle_overlap(b, a)
    return not (a[2] <= b[0] or a[3] <= b[1] or a[1] >= b[3])


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

# Generates the next permutation lexicographically after a given permutation.
# It changes the given permutation in-place.


def next_permutation(arr):
    # Find the highest index i such that s[i] < s[i+1].
    # If no such index exists, the permutation is the last permutation.
    i = len(arr) - 1
    while i > 0:
        if arr[i] > arr[i - 1]:
            break
        i -= 1
    if i == 0:
        return []
    i -= 1

    # Find the highest index j > i such that s[j] > s[i]. Such a j must exist,
    # since i+1 is such an index.
    for j in reversed(range(i + 1, len(arr))):
        if arr[j] > arr[i]:
            break

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree_from_list(lis):
    if len(lis) == 0:
        return None
    root = TreeNode(lis[0])
    st = [root]
    i, j = 0, 1
    while j < len(lis):
        r = st[i]
        i += 1
        if r is None:
            j += 1
        else:
            lv = lis[j]
            r.left = TreeNode(lv) if lv else None
            st.append(r.left)

            if j + 1 >= len(lis):
                break

            rv = lis[j + 1]
            r.right = TreeNode(rv) if rv else None
            st.append(r.right)

            j += 2

    return root


def arr2linkedlist(arr):
    if len(arr) == 0:
        return
    head = ListNode(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


def linkedlist2arr(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


def reverseList(head):
    if not head:
        return head
    pre = None
    cur = None
    while head:
        cur = head.next
        head.next = pre
        pre = head
        head = cur
    return pre


def list_len(head):
    _len = 0
    while head:
        head = head.next
        _len += 1
    return _len


def last_list_value(head):
    v = head.val
    while head:
        v = head.val
        head = head.next
    return v


def is_list_sorted(head):
    if not head:
        return True
    while head.next:
        if head.val > head.next.val:
            return False
        head = head.next
    return True


class Numbers():
    INF = 0x3f3f3f3f
    NEGINF = -0x3f3f3f3f
    #
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#
# https://leetcode.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (28.10%)
# Total Accepted:    22.4K
# Total Submissions: 79.6K
# Testcase Example:  '[2,-1,1,2,2]'
#
# You are given a circular array nums of positive and negative integers. If a
# number k at an index is positive, then move forward k steps. Conversely, if
# it's negative (-k), move backward k steps. Since the array is circular, you
# may assume that the last element's next element is the first element, and the
# first element's previous element is the last element.
#
# Determine if there is a loop (or a cycle) in nums. A cycle must start and end
# at the same index and the cycle's length > 1. Furthermore, movements in a
# cycle must all follow a single direction. In other words, a cycle must not
# consist of both forward and backward movements.
#
#
#
# Example 1:
#
#
# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's
# length is 3.
#
#
# Example 2:
#
#
# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because
# the cycle's length is 1. By definition the cycle's length must be greater
# than 1.
#
#
# Example 3:
#
#
# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle,
# because movement from index 1 -> 2 is a forward movement, but movement from
# index 2 -> 1 is a backward movement. All movements in a cycle must follow a
# single direction.
#
#
#
# Note:
#
#
# -1000 ≤ nums[i] ≤ 1000
# nums[i] ≠ 0
# 1 ≤ nums.length ≤ 5000
#
#
#
#
# Follow up:
#
# Could you solve it in O(n) time complexity and O(1) extra space complexity?
#


class Solution:
    def circularArrayLoop(self, nums):
        for i, n in enumerate(nums):
            mark = str(i)
            """ 1. i is never marked before
            2. one direction
            3. no self-loop
            """
            while (isinstance(nums[i],int)) and (nums[i] * n > 0) and (nums[i] %len(nums) != 0):
                steps = nums[i]
                nums[i] = mark
                i = (i + steps) % len(nums)

            if nums[i] == mark:
                return True

        return False

s = Solution()
nums = [2, -1, 1, 2, 2]
# nums = [-1, 2]
nums = [-2, 1, -1, -2, -2]
nums = [-1, -2, -3, -4, -5]
print(s.circularArrayLoop(nums))


s = Solution()
