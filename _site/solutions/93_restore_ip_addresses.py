'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

'''


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(3):
            for j in range(i + 1, i + 4):
                for m in range(j + 1, j + 4):
                    for n in range(m + 1, m + 4):
                        if m + 1 > len(s) - 1: continue
                        a, b, c, d = s[0:i + 1], s[i + 1:j + 1], s[
                            j + 1:m + 1], s[m + 1:]
                        v = all([self.valid_ip(e) for e in [a, b, c, d]])
                        if v:
                            ans.append(a + "." + b + "." + c + "." + d)
        return list(set(ans))

    def valid_ip(self, s):
        return not (len(s) > 1 and s[0] == '0' or int(s) > 255)


print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("010010"))
