# A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequence:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of array A is called arithmetic if the sequence:
# A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.

# @param {Integer[]} a
# @return {Integer}
def number_of_arithmetic_slices(a)
  return 0 if a.size < 3
  i = r = 0
  j = 2
  while i < a.size - 2
    if j <= a.size - 1 && a[j] - a[j - 1] == a[i + 1] - a[i]
      r += 1
      j += 1
    else
      i += 1
      j = i + 2
    end
  end
  r
end

a = [1, 3, 5, 7, 9]
p number_of_arithmetic_slices(a)
