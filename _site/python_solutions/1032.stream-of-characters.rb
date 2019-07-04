#
# @lc app=leetcode id=1032 lang=ruby
#
# [1032] Stream of Characters
#
# https://leetcode.com/problems/stream-of-characters/description/
#
# algorithms
# Hard (35.61%)
# Total Accepted:    2.4K
# Total Submissions: 6.6K
# Testcase Example:  '["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]\n[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]'
#
# Implement the StreamChecker class as follows:
#
#
# StreamChecker(words): Constructor, init the data structure with the given
# words.
# query(letter): returns true if and only if for some k >= 1, the last k
# characters queried (in order from oldest to newest, including this letter
# just queried) spell one of the words in the given list.
#
#
#
#
# Example:
#
#
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the
# dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the
# wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the
# wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the
# wordlist
#
#
#
#
# Note:
#
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.
#
#
#
require 'set'

class StreamChecker
  #     :type words: String[]
  def initialize(words)
    @stream = {}
    words.each do |w|
      @stream[w[-1]] = Set.new unless @stream.key?(w[-1])
      @stream[w[-1]] << w
      @s = ''
    end
  end

  #     :type letter: Character
  #     :rtype: Boolean
  def query(letter)
    @s += letter
    return false unless @stream.key?(letter)

    @stream[letter].any? { |w| @s.end_with?(w) }
  end
end

# Your StreamChecker object will be instantiated and called as such:
words = %w[cd f kl]
obj = StreamChecker.new(words)
('a'..'l').each do |c|
  p [c, obj.query(c)]
end
