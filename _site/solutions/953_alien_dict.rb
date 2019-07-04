#!/user/bin/env ruby

# @param {String[]} words
# @param {String} order
# @return {Boolean}
def is_alien_sorted(words, order)
  dict = order.chars.zip('a'..'z').to_h
  new_words = words.map { |w| w.chars.map { |c| dict[c] }.join }
  new_words.sort == new_words
end

words = %w[apple app]
order = 'abcdefghijklmnopqrstuvwxyz'
# words = ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
words = %w[hello leetcode]
order = 'hlabcdefgijkmnopqrstuvwxyz'
p is_alien_sorted(words, order)
