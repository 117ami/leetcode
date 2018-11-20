#  Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital if it has more than one letter, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.

# @param {String} word
# @return {Boolean}
def detect_capital_use(word)
  word == word.upcase ||
    word == word.downcase ||
    !(word =~ /^[A-Z]([a-z])*$/).nil?
end

word = 'hellol'
p detect_capital_use(word)
