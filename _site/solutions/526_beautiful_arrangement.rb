#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?
# Example 1:
# Input: 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.
#
#  https://leetcode.com/problems/beautiful-arrangement/description/

# @param {Integer} n
# @return {Integer}
def count_arrangement(n)
  helper = lambda do |m, arr|
    return 1 if m <= 0
    res = 0
    0.upto(m - 1).each do |i|
      next unless arr[i] % m == 0 || m % arr[i] == 0
      arr[i], arr[m - 1] = arr[m - 1], arr[i]
      res += helper.call(m - 1, arr)
      arr[i], arr[m - 1] = arr[m - 1], arr[i]
    end
    return res
  end
  helper.call(n, Array(1..n))
end
p count_arrangement(2)
