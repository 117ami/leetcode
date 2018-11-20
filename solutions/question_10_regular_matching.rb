
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true
def dp(s, p, i, j, memo)
  unless memo.key?([i, j]) # not explored before
    if j == p.length
      ans = i == s.length
    else
      first_match = i < s.length && [s[i], '.'].include?(p[j])
      ans = if j + 1 < p.length && p[j + 1] == '*'
              dp(s, p, i, j + 2, memo) || first_match && dp(s, p, i + 1, j, memo)
            else
              first_match && dp(s, p, i + 1, j + 1, memo)
            end
    end
    memo[[i, j]] = ans
  end
  memo[[i, j]]
end

def is_match(s, p) # question 10 regular expression match
  dp(s, p, 0, 0, {})
end

s10 = 'aaaaabaccbbccababa'
p10 = 'a*b*.*c*c*.*.*.*c'
p is_match(s10, p10)
