#
# Implement a magic directory with buildDict, and search methods.
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
#
#  https://leetcode.com/problems/implement-magic-dictionary/description/
require './aux.rb'
class MagicDictionary
  #     Initialize your data structure here.
  def initialize
    @words = Hash.new { |h, k| h[k] = Hash.new(false) }
  end

  #     Build a dictionary through a list of words
  #     :type dict: String[]
  #     :rtype: Void
  def build_dict(dict)
    dict.each do |word|
      sz = word.size
      @words[sz][word] = true
    end
  end

  #     Returns if there is any word in the trie that equals to the given word after modifying exactly one character
  #     :type word: String
  #     :rtype: Boolean
  def search(word)
    sz = word.size
    return false unless @words.key?(sz)
    @words[sz].keys.any? { |k| ismatch(k, word) }
  end

  def ismatch(sa, sb)
    x = 0
    sa.each_char.with_index do |c, i|
      next if c == sb[i]
      x += 1
      return false if x > 1
    end
    x == 1
  end
end

# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary.new
obj.build_dict(%w[helxo leetcode])
p obj.search('hello')

# dict = Hash.new{|h, k| h[k] = Hash.new(false)}
