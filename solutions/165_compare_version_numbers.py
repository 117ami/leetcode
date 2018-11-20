"""
Compare two version numbers version1 and version2.
If version1 &gt; version2 return 1;&nbsp;if version1 &lt; version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not &quot;two and a half&quot; or &quot;half way to version three&quot;, it is the fifth second-level revision of the second first-level revision.
Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vs1, vs2 = [int(x) for x in version1.split(".")], [
            int(x) for x in version2.split(".")
        ]
        maxlen = max([len(vs1), len(vs2)])
        vs1.extend([0] * 100)
        vs2.extend([0] * 100)
        for i in range(maxlen):
            if vs1[i] < vs2[i]: return -1
            if vs1[i] > vs2[i]: return 1
        return 0


version1 = "7.5.2.4"
version2 = "7.5.3"

# version1 = "1.0.1"
# version2 = "1"

version1 = "0.1"
version2 = "1.1"

# version1 = "01"
# version2 = "1"

s = Solution()
print(s.compareVersion(version1, version2))

arr = list(filter(lambda x: x != 0, range(10)))
print(arr[3:])
