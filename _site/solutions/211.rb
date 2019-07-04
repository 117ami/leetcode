class WordDictionary
  #     Initialize your data structure here.
  def initialize
    @baks = {}
  end

  #     Adds a word into the data structure.
  #     :type word: String
  #     :rtype: Void
  def add_word(word)
    sz = word.size
    @baks[sz] = {} if @baks[sz].nil?
    @baks[sz][word] = nil
  end

  #     Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
  #     :type word: String
  #     :rtype: Boolean
  def search(word)
    sz = word.size
    return false if @baks[sz].nil?
    reg = Regexp.new(word)
    @baks[sz].keys.any? { |w| w.match(reg) }
  end
end

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary.new
obj.add_word('bad')
obj.add_word('mad')
obj.add_word('pad')
p obj.search('.ad')

w = 'bad'
regexp = Regexp.new('..d')
