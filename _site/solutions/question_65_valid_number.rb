
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

# @param {String} s
# @return {Boolean}
def is_number(s)
  s.gsub!(/\s/, '')
  return true if s =~ /\A\d+(\.?)\Z/
  begin
    true if Float(s)
  rescue StandardError
    false
  end
end

p is_number('. 1')

p Float('2e10')
