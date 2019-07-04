# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
# Note: 1 &le; k &le; n &le; 109.
# Example:
# Input:
# n: 13   k: 2
# Output:
# 10
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
#

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_kth_number(n, k)
  return 1 if k == 1
  k -= 1
  curr = 1
  while k > 0
    steps = cal_steps(n, curr, curr + 1)
    if steps <= k
      curr += 1
      k -= steps
    else
      curr *= 10
      k -= 1
    end
  end
  curr
end

def cal_steps(n, n1, n2)
  steps = 0
  while n1 <= n
    steps += [n + 1, n2].min - n1
    n1 *= 10
    n2 *= 10
  end
  steps
end

n = 103
k = 10
p find_kth_number(n, k)
