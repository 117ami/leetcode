# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.
#
# Given a list of query words, return the number of words that are stretchy.
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
# Notes:
#
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters

# @param {String} s
# @param {String[]} words
# @return {Integer}
def to_groups(s)
  cur = s[0]
  stretchy = [cur, 0]
  s.each_char do |c|
    if c == cur
      stretchy[-1] += 1
    else
      stretchy += [c, 1]
      cur = c
    end
  end
  stretchy
end

def expressive_words(s, words)
  return 0 if s.length.zero?
  stretchy = to_groups(s)
  r = 0
  words.each do |w|
    tmp = to_groups(w)
    next if tmp.size != stretchy.size
    flag = true
    (0..tmp.size - 1).each do |i|
      if i.even?
        next if tmp[i] == stretchy[i]
        flag = false
        break
      else
        next if stretchy[i] >= 3 && stretchy[i] > tmp[i] || stretchy[i] == tmp[i]
        flag = false
        break
      end
    end
    p [w, flag]
    r += 1 if flag
  end
  r
end

s = 'heeellooo'
words = %w[helo hi hello]
p expressive_words(s, words)
