#!/usr/bin/ruby -w
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).

# @param {String} s
# @param {String[]} words
# @return {Integer[]}
def find_substring(s, words)
  return [0..s.size - 1] if words.empty?
  return [] if s.size < words[0].size
  hash = Hash.new(0).tap { |h| words.each { |v| h[v] += 1 } }

  strlen = s.length
  wordslen = words.size
  len = words.first.length
  i = 0
  res = []
  while i <= strlen - wordslen * len
    j = 0
    seen = Hash.new(0)
    while j <= (wordslen - 1) * len
      substr = s[i + j..i + j + len - 1]
      seen[substr] += 1
      break if seen[substr] > hash[substr]
      j += len
    end
    res.push(i) if j == wordslen * len
    i += 1
  end
  res
end

p find_substring('thebarfoofoobarthefoobarman', %w[foo bar the])
# p find_substring(s, words) #
