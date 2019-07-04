#
# Given a sorted array, two integers k and x, find the k closest elements to x in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
#  Length of the given array is positive and will not exceed 104
#
#  Absolute value of elements in the array and x will not exceed 104
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
#
# @param {Integer[]} arr
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_closest_elements(arr, k, x)
  index = (0..arr.size - 1).bsearch { |i| arr[i] > x } || arr.size - 1
  i = index - 1
  j = index
  while k > 0
    if i < 0 || (j < arr.size && (arr[i] - x).abs > (arr[j] - x).abs)
      j += 1
    else
      i -= 1
    end
    k -= 1
  end
  arr[i + 1..j - 1]
end

arr = [1] # , 2, 3, 5, 6, 7, 8]
p find_closest_elements(arr, 1, 1)
