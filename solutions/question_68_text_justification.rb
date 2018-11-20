
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.
#
# click to show corner cases.

# @param {String[]} words
# @param {Integer} max_width
# @return {String[]}
def full_justify(words, max_width)
  r = [[words.shift]]
  x = r[0][0].length + 1
  words.each do |w|
    if x + w.length <= max_width
      r[-1] << w
      x += (1 + w.length)
    else
      x = w.length + 1
      r << [w]
    end
  end

  last = left_justified(r[-1], max_width)
  r = r[0..-2].map { |v| justify(v, max_width) }
  r << last
end

def justify(v, wid)
  vs = v.size
  len = v.join.length
  return v[0] + ' ' * (wid - len) if vs == 1
  return v.join(' ' * (wid - len)) if vs == 2
  0.upto(wid) do |i|
    i = i % vs
    v[i] += ' '
    len += 1
    return v.join if len == wid
  end
end

def left_justified(v, wid)
  r = v.join(' ')
  r += ' ' * (wid - r.length)
end

words = 'This is an example of text justification. okay de la'.split(/\s/)
words = 'a b b b c df e global okay ?'.split(/\s/)
# words = 'what must be shall be.'.split(/\s/)
# words = ['abc', 'efg']
p full_justify(words, 12)
