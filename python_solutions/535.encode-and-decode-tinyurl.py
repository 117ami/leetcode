from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
import itertools 
import math 
import string
true = True
false = False
MIN, MAX = -0x3f3f3f3f, 0x3f3f3f3f
#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (78.89%)
# Total Accepted:    98.1K
# Total Submissions: 124.3K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
# 
#
class Codec:
    def __init__(self):
        self.db = [] 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.db.append(longUrl)
        return 'https://tinyurl.com/' + str(len(self.db))
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        l = int(shortUrl.split('/')[-1])
        return self.db[l-1]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://www.google.com"
print(codec.decode(codec.encode(url)))




