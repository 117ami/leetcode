#
# @lc app=leetcode id=925 lang=ruby
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.26%)
# Total Accepted:    14K
# Total Submissions: 31.7K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
#
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
#
#
#
# Example 1:
#
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
#
#
#
# Example 2:
#
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
#
#
#
# Example 3:
#
#
# Input: name = "leelee", typed = "lleeelee"
# Output: true
#
#
#
# Example 4:
#
#
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
#
#
#
#
#
#
#
# Note:
#
#
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
#
#
#
#
#
#
#
#
#
#
#
#
# @param {String} name
# @param {String} typed
# @return {Boolean}
def is_sub?(s, t)
  i = j = 0
  while i < s.size && j < t.size
    i += 1 if s[i] == t[j]
    j += 1
  end
  i == s.size
end

def is_long_pressed_name(nname, typed)
  is_sub?(nname, typed)
end

nname = 'alex'
typed = 'aaleex'
nname = 'kikcxmvzi'
typed = 'kiikcxxmmvvzz'
p is_long_pressed_name(nname, typed)
