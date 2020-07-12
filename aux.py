from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007
from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
from random import randint
import random
import collections
from bisect import bisect_left


class FenwickTree:
    def __init__(self, _size):
        self.tree = [0] * _size

    def prefix_sum(self, i):
        _sum = 0
        while i > 0:
            _sum += self.tree[i]
            i -= (i & (-i))
        return _sum

    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += (i & (-i))


class XString(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if s == s[::-1]: return n
        cur = [0] * n

        for i in range(len(s))[::-1]:
            pre = cur[:]
            cur[i] = 1
            for j in range(i + 1, n):
                cur[j] = 2 + pre[j - 1] if s[i] == s[j] else max(cur[j - 1], pre[j])
        return cur[-1]

    def is_p(self, s):
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

    def find_all_lcs(self, s, t):
        """ Find all lcs whether there are multiple choices
        return type: set<string>
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

        def helper(i, j):
            res = set()
            if i == 0 or j == 0:
                res.add("")
                return res

            if s[i - 1] == t[j - 1]:
                tmp = helper(i - 1, j - 1)
                for rs in tmp:
                    res.add(rs + s[i - 1])
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    res = helper(i - 1, j)

                if dp[i - 1][j] <= dp[i][j - 1]:
                    tmp = helper(i, j - 1)
                    for rs in tmp:
                        res.add(rs)
            return res

        return helper(m, n)

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
                part[i][j] = part[i][j] or part[i - nums[j - 1]][j - 1]

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


def print_tree(root):
    nodes = []

    def dfs(r, d):
        if not r:
            return
        if len(nodes) <= d:
            nodes.append([])
        nodes[d].append(r.val)
        dfs(r.left, d + 1)
        dfs(r.right, d + 1)

    dfs(root, 0)

    for arr in nodes:
        print(arr)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


class Trees:
    def inorder(self, root):
        """ A very fast way of traversal tree inorder
        """
        def rec(node):
            if node.left:
                for other in rec(node.left):
                    yield other
            yield node
            if node.right:
                for other in rec(node.right):
                    yield other

        for node in rec(root):
            yield node

    def getdepth(self, r):
        if not r:
            return 0
        return 1 + max(self.getdepth(r.left), self.getdepth(r.right))

    def printTree(self, root):
        self.d = self.getdepth(root)
        width = 2**self.d - 1
        res = [[""] * width for _ in range(self.d)]

        def dfs(node, depth, loc):
            if not node or depth > self.d:
                return
            res[depth - 1][loc] = str(node.val)
            offset = 2 ** (self.d - depth - 1)
            dfs(node.left, depth + 1, loc - offset)
            dfs(node.right, depth + 1, loc + offset)

        dfs(root, 1, width // 2)
        for layer in res:
            print(layer)
        return res

    def listToTree(self, arr):
        """Build tree for a list. E.g., [1,2,3,None,4]
        """
        if not arr:
            return
        children = 0
        i = 1
        jobs = [TreeNode(arr[0])]
        root = jobs[0]
        while i < len(arr):
            if children == 2:
                jobs.pop(0)
                children = 0

            if arr[i] is not None:
                c = TreeNode(arr[i])
                if children == 0:
                    jobs[0].left = c
                else:
                    jobs[0].right = c
                jobs.append(c)

            children += 1
            i += 1

        return root

    def sortedArrayToBST(self, arr):
        if not arr: return 
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root 

    def treeToList(self, root):
        """Encodes a tree to a list
        :type root: TreeNode
        :rtype: list[int]
        """
        if not root: return []
        jobs, res = [root], []
        while jobs:
            r = jobs.pop(0)
            if r:
                res.append(r.val)
                jobs += [r.left, r.right]
        return res


    def isCompleteTree(self, root: TreeNode) -> bool:
        """ Whether a given a tree is complete
        """
        if not root:
            return True
        stack = [root]
        self.empty = False

        while stack:
            n = stack.pop(0)
            if not n:
                self.empty = True
            if n is None and len(stack) > 0 and stack[-1] is not None:
                return False
            if n:
                if self.empty:
                    return False
                # print(n.val, self.empty)
                stack.append(n.left if n.left else None)
                stack.append(n.right if n.right else None)

        return True


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


def intToRoman(self, num: int) -> str:
    """Convert a given integer to a roman numeral
    """
    res = ""
    m = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}
    for k in m:
        d, num = divmod(num, k)
        res += m[k] * d
    return res


def create_palindrome(inp, b, is_odd):
    n = inp
    palin = inp

    # checks if number of digits is odd or even
    # if odd then neglect the last digit of input in
    # finding reverse as in case of odd number of
    # digits middle element occur once
    if is_odd:
        n = n // b

    # Creates palindrome by just appending reverse
    # of number to itself
    while n > 0:
        palin = palin * b + (n % b)
        n = n // b
    return palin

def generate_palindromes(n):
    '''Generate all palindromic numbers less than n'''
    # Run two times for odd and even length palindromes
    ans = set()
    for j in range(2):
        # Creates palindrome numbers with first half as i.
        # Value of j decided whether we need an odd length
        # of even length palindrome.
        i = 1
        r = 1
        while r < n:
            ans.add(r)
            r = create_palindrome(i, 10, j % 2)
            i += 1
    return ans 


def sieve_primes(n):
    """ Find all primes under (inclusive) n
    """
    tables = []
    bool_tables = [True] * (1 + n)
    for i in range(2, n + 1):
        if bool_tables[i]:
            tables.append(i)
            for j in range(i << 1, n + 1, i):
                bool_tables[j] = False
    return tables


def isprime(x):
    """Combining sieve_primes to decide whether a
    given number is prime
    """
    n = 1 + int(x ** 0.5)
    bool_tables = [True] * (1 + n)
    for i in range(2, n + 1):
        if bool_tables[i]:
            if x % i == 0:
                return False

            for j in range(i << 1, n + 1, i):
                bool_tables[j] = False
    return True


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.p[px] = self.p[py] = min(px, py)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


def getPrefixSum(mat):
    """ Compute the prefixSum matrix, where prefix_sum[i][j] is the sum of submatrix mat[0...i][0...j]
    """
    m, n = len(mat), len(mat[0])
    x = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                x[i][j] = mat[0][0]
            elif i == 0:
                x[i][j] = mat[0][j] + x[i][j-1]
            elif j == 0:
                x[i][j] = mat[i][0] + x[i-1][j]
            else:
                x[i][j] = x[i-1][j] + x[i][j-1] - x[i-1][j-1] + mat[i][j] 
    return x 


# Floyd Warshell algorithm, n nodes
def floyd_warshell(n, edges):
    dis = [[float('inf')] * n for _ in range(n)]
    for i, j, w in edges:
        dis[i][j] = dis[j][i] = w
    
    for i in range(n):
        dis[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])


def string_date_to_number(date):
    import time 
    import datetime
    return time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())


def flatten(nested_list):
    """Flatten a list of nested list / tuple into one single list"""
    res = []
    for e in nested_list:
        if type(e) == list or type(e) == tuple:
            res.extend(flatten(e))
        else:
            res.append(e)
    return res 


class KMP():
    def get_lhp(self, t: str) -> List[int]:
        '''Compute the length of LHP for each t[:i], i \in [1..len(t)],
        where a prefix-suffix of t is a substring, u, of t s.t., t.startswith(u) and t.endswith(u).
        And proper means, len(u) < len(t), i.e., u != t
        '''
        j, lhp = 0, [0] * len(t)
        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lhp[j-1]
                
            if t[i] == t[j]:
                j += 1
                lhp[i] = j
        return lhp

    def pattern_search(self, text: str, pat: str) -> List[int]:
        """KMP (Knuth Morris Pratt) Pattern Searching
        Return a list of indexes i, such that t occurs in s starting from i.
        """
        j = 0
        lhp, res = self.get_lhp(pat), []
        for i in range(len(text)):
            while j > 0 and text[i] != pat[j]:
                j = lhp[j-1]

            if text[i] == pat[j]:
                j += 1 

            if j == len(pat):
                res.append(i + 1 - len(pat))
                j = lhp[j - 1]
        return res

sol = Solution()



sol = Solution()


print(sol.__init__())
print(sol.prefix_sum())
print(sol.update())
print(sol.longestPalindromeSubseq())
print(sol.is_p())
print(sol.lcslen())
print(sol.lcs())
print(sol.find_all_lcs())
print(sol.scs())
print(sol.__init__())
print(sol.__str__())
print(sol.isEmpty())
print(sol.size())
print(sol.push())
print(sol.pop())
print(sol.__init__())
print(sol.__init__())
print(sol.inorder())
print(sol.getdepth())
print(sol.printTree())
print(sol.listToTree())
print(sol.sortedArrayToBST())
print(sol.treeToList())
print(sol.isCompleteTree())
print(sol.intToRoman())
print(sol.__init__())
print(sol.union())
print(sol.find())
print(sol.get_lhp())
print(sol.pattern_search())
