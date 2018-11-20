
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# First the first (equal) higher map on the right side of higher[id].
# The map can not be adjacent to height[id]
def first_higher(height, id)
  return nil if id < height.size - 1 && height[id + 1] >= height[id]
  r = nil
  max = -1
  (id + 1).upto(height.size - 1).each do |i|
    return i if height[i] >= height[id]
    if height[i] > max
      max = height[i]
      r = i
    end
  end
  r
end

# Compute the trapped water between i and j, assuming j > i and height[j] >= height[i]
#  and no other higher cap is interleaving.
def sum(height, i, j)
  r = (j - i - 1) * [height[i], height[j]].min
  (i + 1).upto(j - 1).each { |k| r -= height[k] }
  r
end

# @param {Integer[]} height
# @return {Integer}
def trap(height)
  return 0 if height.empty?
  r = 0
  i = 0
  loop do
    break if i >= height.size - 1
    while (j = first_higher(height, i)).nil?
      i += 1
      return r if i >= height.size - 2
    end
    r += sum(height, i, j)
    print "i, j, sum: #{i}, #{j}, #{r}\n"
    i = j
  end
  r
end

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 3]
# height = [5,4,1,2]
p trap(height)
