# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
# Example 1:
# Input: "bcabc"
# Output: "abc"
# Example 2:
# Input: "cbacdcbc"
# Output: "acdb"
#
#  https://leetcode.com/problems/remove-duplicate-letters/description/
require './aux.rb'

# @param {String} s
# @return {String}
def remove_duplicate_letters(s)
  res = []
  greedy = lambda do |xs|
    return if xs.length.zero?
    cnt = Hash.new(0).tap { |h| xs.each_char { |c| h[c] += 1 } }
    pos = 0
    0.upto(xs.size - 1).each do |i|
      pos = i if xs[i] < xs[pos]
      cnt[xs[i]] -= 1
      next unless cnt[xs[i]].zero?
      res << xs[pos]
      break
    end
    xs.gsub!(/#{xs[pos]}/, '')
    greedy.call(xs[pos..-1])
  end
  greedy.call(s)
  res.join
end

s = 'cbacdcbc'
s = 'bcabc'
p remove_duplicate_letters(s)
