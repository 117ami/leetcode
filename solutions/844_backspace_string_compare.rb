# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
  bs = lambda do |string|
    stack = []
    string.each_char do |c|
      stack.pop if c == '#'
      stack << c unless c == '#'
    end
    stack.join('')
  end

  bs.call(t) == bs.call(s)
end

s = '#a#b'
t = 'a'
p backspace_compare(s, t)
