
# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  sz = nums.size - 1
  (0..sz).each do
    if nums[0] == val
      nums.shift
    else
      nums.push(nums.shift)
    end
  end
  nums.size
end

remove_element([3, 2, 2, 3], 3)
remove_element([1, 2, 4, 3, 2, 2, 3], 3)
