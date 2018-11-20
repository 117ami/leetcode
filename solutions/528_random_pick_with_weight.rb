# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
#

class Solution
  #     :type w: Integer[]
  def initialize(w)
    @idxs = []
    @xsum = 0
    w.each_with_index do |n, i|
      @xsum += n
      @idxs << [i, @xsum]
    end
  end

  #     :rtype: Integer
  def pick_index
    k = Random.rand(@xsum)
    i = (0..@idxs.size - 1).bsearch { |j| @idxs[j].last > k }
    @idxs[i].first
    # @idxs
  end
end

# Your Solution object will be instantiated and called as such:
w = [1, 3, 2, 4]
obj = Solution.new(w)
10.times { p obj.pick_index }
