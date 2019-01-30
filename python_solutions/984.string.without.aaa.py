"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"
 

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B."""

class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == 0: return 'b' * B
        if B == 0: return 'a' * A 
        if A == B: return 'ab' * A 
        if A > B: return 'aab' + self.strWithout3a3b(A-2, B-1)
        return self.strWithout3a3b(A-1, B-2) + 'abb'

print(Solution().strWithout3a3b(3, 6))