'''
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"
Output: "012"
Example 2:
Input: "fviefuro"
Output: "45"
'''
import collections
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        letters = collections.Counter([x for x in s])
        self.decode('z', '0', 'zero', res, letters)
        self.decode('w', '2', 'two', res, letters)
        self.decode('x', '6', 'six', res, letters)
        self.decode('u', '4', 'four', res, letters)
        self.decode('g', '8', 'eight', res, letters)
        self.decode('h', '3', 'three', res, letters)
        self.decode('f', '5', 'five', res, letters)
        self.decode('s', '7', 'seven', res, letters)
        self.decode('o', '1', 'one', res, letters)
        self.decode('i', '9', 'nine', res, letters)
        res.sort()
        return ''.join(res)


    def decode(self, c, n, word, res, letters):
        if c not in letters or letters[c] == 0: return
        res.extend([n] * letters[c])
        k = letters[c]
        for x in word:
            letters[x] -= k



sol = Solution()
print (sol.originalDigits("onetthreefourwo"))
# res = []
# res.append(3) 
# print(res)
