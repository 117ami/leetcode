# We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?
#
# Note that our partition must use every number in A, and that scores are not necessarily integers.
#
# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

# @param {Integer[]} a
# @param {Integer} k
# @return {Float}
def largest_sum_of_averages(a, k)
  sums = Array.new(a.size + 1, 0)
  a.each_with_index { |n, i| sums[i] = sums[i - 1] + n }
  res = Array.new(a.size + 1) { Array.new(k + 1, 0) }

  (1..a.size).each do |i|
    (1..k).each do |j|
      if i == j
        res[i][j] = sums[i - 1]
      elsif j == 1
        res[i][j] = sums[i - 1] * 1.0 / i
      else
        (j - 1..i - 1).each do |m|
          res[i][j] = [res[i][j], res[m][j - 1] + (sums[i - 1] - sums[m - 1]) * 1.0 / (i - m)].max
        end
      end
    end
  end
  res[a.size][k]
end

a = [9, 1, 2, 3, 9]
a = [4, 1, 7, 5, 6, 2, 3]
# a = [4663, 3020, 7789, 1627, 9668, 1356, 4207, 1133, 8765, 4649, 205, 6455, 8864, 3554, 3916, 5925, 3995, 4540, 3487, 5444, 8259, 8802, 6777, 7306, 989, 4958, 2921, 8155, 4922, 2469, 6923, 776, 9777, 1796, 708, 786, 3158, 7369, 8715, 2136, 2510, 3739, 6411, 7996, 6211, 8282, 4805, 236, 1489, 7698]
k = 4
p largest_sum_of_averages(a, k)
