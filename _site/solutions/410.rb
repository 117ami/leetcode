# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer}
def split_array(nums, m)
  amax = nums.max
  asum = nums.reduce(:+)
  return asum if m == 1

  valid = lambda do |target|
    cter = 1
    total = 0
    nums.each do |n|
      total += n
      next if total <= target
      total = n
      cter += 1
      return false if cter > m
    end
    true
  end

  while amax <= asum
    mid = (amax + asum) / 2
    if valid.call(mid)
      asum = mid - 1
    else
      amax = mid + 1
    end
  end
  amax
end

nums = [7, 2, 5, 10, 8]
m = 2
p split_array(nums, m)
