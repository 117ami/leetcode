# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
#     B.length >= 3
#     There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.
#
# Example 1:
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
# Example 2:
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
# Note:
#
#     0 <= A.length <= 10000
#     0 <= A[i] <= 10000

# @param {Integer[]} a
# @return {Integer}
def longest_mountain(a)
  return 0 if a.size < 3
  i = 0
  i += 1 while i < a.size - 1 && a[i + 1] <= a[i]
  return 0 if i == a.size - 1
  maxlen = 0
  down = false

  a.each_with_index do |n, j|
    next if j <= i
    p [i, j, maxlen]
    if n == a[j - 1]
      i = j
      i += 1 while i < a.size - 1 && a[i + 1] <= a[i]
    elsif n < a[j - 1]
      maxlen = [maxlen, j - i + 1].max
      down = true
    elsif n > a[j - 1] && down
      i = j - 1
      down = false
    end
  end
  maxlen
end

def longest_mountain2(a)
  return 0 if a.size < 3
  submits = Array(1..a.size - 2).select { |i| a[i - 1] < a[i] && a[i] > a[i + 1] }
  maxlen = 0
  submits.each do |h|
    i = j = h
    i -= 1 while i > 0 && a[i] > a[i - 1]
    maxlen = [maxlen, j - i + 1].max

    j += 1 while j < a.size - 1 && a[j] > a[j + 1]
    maxlen = [maxlen, j - i + 1].max
  end
  maxlen
end

a = [2, 1, 4, 7, 3, 2, 5]
# a = [2, 2, 2]
# a = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a = [2, 3, 3, 2, 0, 2]
a = [0, 1, 0, 2, 2]
p longest_mountain(a)
p longest_mountain2(a)
