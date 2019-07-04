# A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.
#
# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
#
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
#
# Input: A = [1, 7], K = 1
# Output: [1, 7]
# Note:
#
# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length + 1) / 2.

# @param {Integer[]} a
# @param {Integer} k
# @return {Integer[]}
def kth_smallest_prime_fraction(a, k)
  high = 1.0
  low = m = n = 0
  while high - low > 1.0e-8
    mid = (high + low) / 2.0
    bool, vm, vn = below?(mid, a, k)
    if bool
      low = mid
      if m.zero? || m * vn < vm * n
        m = vm
        n = vn
      end
    else
      high = mid
    end
  end
  [m, n]
end

def below?(v, a, k)
  # The number of fraction with value no bigger than v is no more than k
  count = i = j = m = n = 0
  while i < a.size - 1 && j < a.size
    if a[i] <= a[j] * v
      count += a.size - j
      m, n = a.values_at(i, j) if m.zero? || m * a[j] < a[i] * n
      i += 1
      j += 1 if i > j
    else
      j += 1
    end
  end
  [count <= k, m, n]
end

a = [1, 2, 3, 5] # , 7, 11]
p kth_smallest_prime_fraction(a, 3)
