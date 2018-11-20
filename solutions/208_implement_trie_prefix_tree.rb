# Implement a trie with insert, search, and startsWith methods.
# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:
#   You may assume that all inputs are consist of lowercase letters a-z.
#   All inputs are guaranteed to be non-empty strings.
#
#  https://leetcode.com/problems/implement-trie-prefix-tree/description/
require './aux.rb'

class Trie
  #     Initialize your data structure here.
  def initialize
    @strings = {}
  end

  #     Inserts a word into the trie.
  #     :type word: String
  #     :rtype: Void
  def insert(word)
    first_letter = word[0]
    @strings[first_letter] = {} if @strings[first_letter].nil?
    @strings[first_letter][word] = true
  end

  #     Returns if the word is in the trie.
  #     :type word: String
  #     :rtype: Boolean
  def search(word)
    fl = word[0]
    return false if @strings[fl].nil? || @strings[fl][word].nil?
    true
  end

  #     Returns if there is any word in the trie that starts with the given prefix.
  #     :type prefix: String
  #     :rtype: Boolean
  def starts_with(prefix)
    fl = prefix[0]
    return false if @strings[fl].nil?
    @strings[fl].keys.any? { |k| k.start_with?(prefix) }
  end
end

# Your Trie object will be instantiated and called as such:
obj = Trie.new
obj.insert('apple')
p obj.starts_with('pple')
p obj.search('app')

obj.insert('app')
p obj.search('app')
