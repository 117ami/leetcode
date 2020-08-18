
class Solution {
public:
  // Given a string S and a string T, find the minimum window in S which will
  // contain all the characters in T in complexity O(n).
  string minWindow(string_view s, string_view t) {
    int cnt = t.size();
    int cc[128] = {0};
    for (auto c : t)
      cc[c]++;
    int start = 0, end = INT_MAX, left = 0;

    for (int i = 0; i < s.size(); i++) {
      if (cc[s[i]] > 0) cnt--;
      cc[s[i]]--;

      if (cnt == 0) {
        while (left < i && cc[s[left]] < 0) {
          cc[s[left]]++;
          left++;
        }
        if (i - left < end - start)
          start = left, end = i;
      }
    }
    return end < INT_MAX ? string(s.substr(start, end - start + 1)) : "";
  }
};
