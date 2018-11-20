# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
#
# @param {String} s
# @return {Integer}
def first_uniq_char(s)
  fre = Hash.new(0).tap { |h| s.each_char { |c| h[c] += 1 } }
  s.each_char.with_index do |c, i|
    return i if fre[c] == 1
  end
  -1
end

p first_uniq_char('leetcode')
p first_uniq_char('loveleetcode' * 100000)
