
# String to Integer (atoi)
# Implement atoi to convert a string to an integer.

# Return TRUE if string is empty or starts with illegal characters
def invalid_string(str)
  return true if str.strip! == ''
  return true unless str[0] =~ /[0-9\+\-]/
  false
end

# A valid integer must be between -2**31 - 2**31 - 1
def format_int(n)
  return - 2**31 if n < -2**31
  return 2**31 - 1 if n > 2**31 - 1
  n
end

def q8(str)
  return 0 unless /^\s*(?<snum>[+-]?\d+)/ =~ str
  unless snum[0] =~ /[0-9]/
    sign = -1 if snum[0] == '-'
    snum[0] = ''
  end
  sign = 1 if sign.nil?
  
  res = snum.chars.inject(0) { |p, n| p * 10 + n.to_i } * sign
  format_int(res)
end

str8 = ' 1  xdkd'
#str8 = ' 1 '
if /^\s*(?<anum>[+-]?\d+)/ =~ str8
  print anum, "==yes! with sign \n"
else
  print "illegal string!", anum.nil?
end

p q8(str8)
