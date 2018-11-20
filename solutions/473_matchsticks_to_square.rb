# @param {Integer[]} nums
# @return {Boolean}
def makesquare(nums)
  nsum = nums.reduce(:+)
  return false if nums.size < 4 || nsum % 4 > 0
  edge_len = nsum / 4
  nums.sort!.reverse!
  dict = Hash.new(0).tap { |h| nums.each { |n| h[n] += 1 } }
  dfs(nums, [0, 0, 0, 0], 0, edge_len)
end

def dfs(nums, ans, idx, edge_len)
  return ans.all? { |e| e == edge_len } if idx == nums.size
  ans.each_index do |i|
    next if ans[i] + nums[idx] > edge_len
    ans[i] += nums[idx]
    return true if dfs(nums, ans, idx + 1, edge_len)
    ans[i] -= nums[idx]
  end
  false
end

def helper(dict, edge_len)
  if dict[edge_len] > 0
    dict[edge_len] -= 1
    return true
  end
  dict.each_key do |k|
    next if k > edge_len || dict[k].zero?
    dict[k] -= 1
    return true if helper(dict, edge_len - k)
    dict[k] += 1
  end
  false
end

nums = [1, 7, 2, 4, 5, 5]
nums = [2, 3, 4, 5, 7, 9, 15, 15]
# nums = [3, 3, 3, 3, 4]
# nums = [7215807,6967211,5551998,6632092,2802439,821366,2465584,9415257,8663937,3976802,2850841,803069,2294462,8242205,9922998]

p makesquare(nums)
