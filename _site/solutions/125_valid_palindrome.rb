# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
# Example 2:
#
# Input: "race a car"
# Output: false

# @param {String} s
# @return {Boolean}
def is_palindrome(s)
  s.gsub!(/\W/, '').downcase!
  s == s.reverse
end

s = 'A man, a plan, a canal: Panama'
s = 'race a car'
p is_palindrome(s)
