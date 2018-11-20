# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# @param {Integer[]} nums
# @return {String[]}
def find_relative_ranks(nums)
  ranks = nums.sort.reverse.zip(['Gold Medal', 'Silver Medal', 'Bronze Medal'].concat(Array(4..nums.size))).to_h
  nums.map { |n| ranks[n].to_s }
end

nums = 11.times.map { Random.rand(100) }
p nums
p find_relative_ranks(nums)
