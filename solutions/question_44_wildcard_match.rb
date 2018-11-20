#     Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
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
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
  ids = 0
  idp = 0
  idm = 0
  idstar = -1
  while ids < s.length
    if idp < p.length && (p[idp] == '?' || p[idp] == s[ids])
      idp += 1
      ids += 1
    elsif idp < p.length && p[idp] == '*'
      idstar = idp
      idm = ids
      idp += 1
    elsif idstar != -1
      idp = idstar + 1
      idm += 1
      ids = idm
    else
      return false
    end
  end

  idp += 1 while idp < p.length && p[idp] == '*'
  idp == p.length
end

s = 'aabccac'
p = 'a*bc*ac'
p is_match('aa', '*')
