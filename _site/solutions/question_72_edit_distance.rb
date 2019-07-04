
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character

# http://www.stanford.edu/class/cs124/lec/med.pdf
# stanford cs class on this problem
# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
  m = word1.length
  n = word2.length
  d = Array.new(m + 1){ Array.new(n + 1, -1) }
  (0..n).each { |i| d[0][i] = i }
  (0..m).each { |i| d[i][0] = i }

  1.upto(m) do |i|
    1.upto(n) do |j|
      next if d[i][j] >= 0
      x = word1[i - 1] == word2[j - 1] ? 0 : 1
      d[i][j] = [x + d[i - 1][j - 1], d[i - 1][j] + 1, d[i][j - 1] + 1].min
    end
  end
  d[m][n]
end

p min_distance('aeiou', 'aieou')
p min_distance('', '')


