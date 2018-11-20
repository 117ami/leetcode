# Design a class to findthe kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# YourKthLargestclass will have a constructor which accepts an integer k and an integer array nums, which contains initial elements fromthe stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
# Example:
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3); // returns 4
# kthLargest.add(5); // returns 5
# kthLargest.add(10); // returns 5
# kthLargest.add(9); // returns 8
# kthLargest.add(4); // returns 8
# Note:
# You may assume thatnums' length>=k-1and k >=1.
#
#  https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
require './aux.rb'

class KthLargest
  def initialize(k, nums)
    @arr = nums.sort
    @idx = k
  end

  #     :type val: Integer
  #     :rtype: Integer
  def add(val)
    locidx = (0..@arr.size - 1).bsearch { |i| @arr[i] >= val } || @arr.size
    @arr.insert(locidx, val)
    @arr[-@idx]
  end
end

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest.new(k, nums)
# param_1 = obj.add(val)
arr = [4, 5, 8, 2]
k = 3
obj = KthLargest.new(k, arr)
[3, 5, 10, 9, 4].each do |n|
  p obj.add(n)
end
