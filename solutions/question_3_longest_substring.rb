
# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  return 0 if s.size.zero?
  res = 1
  arr = []
  s.split('').each do |e|
    if arr.include?(e)
      id = arr.index(e) + 1
      arr.slice!(0, id)
    end
    arr.push(e)
    res = [res, arr.size].max
  end
  res
end

# redo this problem at 2/7/2018
def length_of_longest_substring_2(s)
  loc = Hash.new(-1)
  start = 0
  maxlen = 0
  s.each_char.with_index do |c, i|
    start = [start, loc[c] + 1].max
    loc[c] = i
    maxlen = [maxlen, i - start + 1].max
  end
  maxlen
end

p length_of_longest_substring_2('abba')
