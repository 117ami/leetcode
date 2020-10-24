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
import math, re
import heapq 
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007



# https://leetcode.com/problems/web-crawler/description/
# Medium
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = {}
        visited[startUrl] = True
        q = deque()
        q.append(startUrl)
        domain = re.findall(r'http://(.*?)/', startUrl + "/")[0]

        while q:
            url = q.popleft()
            for nxt in htmlParser.getUrls(url):
                if nxt.startswith(f'http://{domain}') and nxt not in visited:
                    visited[nxt] = True
                    q.append(nxt)
        return list(visited)

url = "http://news.yahoo.com/news/topics/"
domain = re.findall(r'http://(.*?)/', url)
print(domain)