# Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
# A student attendance record is a string that only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
#  'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# Example 1:
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
# Note:
# The value of n won't exceed 100,000.
#
#  https://leetcode.com/problems/student-attendance-record-ii/description/

# @param {Integer} n
# @return {Integer}
def check_record(n)
  return 3 if n == 1
  return 8 if n == 2
  return 19 if n == 3

  ea = [1, 2, 4]
  ep = [1, 3, 8]
  el = [1, 3, 7]
  mod = 10**9 + 7
  3.upto(n - 1).each do |i|
    ea[i] = (ea[i - 1] + ea[i - 2] + ea[i - 3]) % mod
    ep[i] = (ea[i - 1] + ep[i - 1] + el[i - 1]) % mod
    el[i] = (ea[i - 1] + ep[i - 1] + ea[i - 2] + ep[i - 2]) % mod
  end
  (ea.last + ep.last + el.last) % mod
end

def valid_string(s)
  s !~ /lll|a.*a/
end

def bruteforce(n)
  items = %w[a p l]
  res = 0
  xn = 0
  items.repeated_permutation(n).each do |s|
    res += 1 if valid_string(s.join)
    sss = s.join
    xn += 1 if valid_string(sss) && sss =~ /la$/
    # p sss if valid_string(sss) && sss =~ /la$/
  end
  res
end

10.times.each do |_|
  n = Random.rand(100_000)
  p [n, check_record(n)]
  # p bruteforce(n)
end
