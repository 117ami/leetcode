# Given a blacklistB containing unique integersfrom [0, N), write a function to return a uniform random integer from [0, N) which is NOTin B.
# Optimize it such that it minimizes the call to system&rsquo;s Math.random().
# Note:
#   1 <= N <= 1000000000
#   0 <= B.length < min(100000, N)
#   [0, N)does NOT include N. See interval notation.
# Example 1:
# Input:
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
# Example 2:
# Input:
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
# Example 3:
# Input:
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
# Example 4:
# Input:
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
# Explanation of Input Syntax:
# The input is two lists:the subroutines calledand theirarguments.Solution'sconstructor has two arguments,N and the blacklist B. pick has no arguments.Argumentsarealways wrapped with a list, even if there aren't any.
#
#  https://leetcode.com/problems/random-pick-with-blacklist/description/
require './aux.rb'

class Solution
  #     :type n: Integer
  #     :type blacklist: Integer[]
  def initialize(n, blacklist)
    @n = n
    @sz = blacklist.size
    @avail = {}
    @unavail = blacklist.zip([nil]).to_h
    if @sz >= n / 2
      @avail = (0..@n - 1).zip([nil]).to_h
      blacklist.each { |k| @avail.delete(k) }
      @avail = @avail.keys
    end
  end

  #     :rtype: Integer
  def pick
    return @avail.sample if @sz >= @n / 2
    res = Random.rand(@n)
    @unavail.key?(res) ? pick : res
  end
end

# Your Solution object will be instantiated and called as such:
n = 5_000_000
n = 10_000
blacklist = (1..9990).to_a
obj = Solution.new(n, blacklist)
10.times { p obj.pick }
