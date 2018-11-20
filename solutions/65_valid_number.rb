# Validate if a given string is numeric.
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
#
#  https://leetcode.com/problems/valid-number/description/
require './aux.rb'

# @param {String} s
# @return {Boolean}
def is_number(s)
  s.lstrip!
  s.rstrip! 
  (s =~ /^[-+]?(\d+\.?|\.\d+)\d*(e[-+]?\d+)?$/).nil? ? false : true
end

s = '   .1 '
s = '0'
p is_number(s)
