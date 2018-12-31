# @param {Integer[]} nums
# @return {Boolean}
def is_possible(nums)
  freqs = nums.each_with_object(Hash.new(0)) { |w, h| h[w] += 1; }
  terminates = Hash.new(0)
  nums.each do |n|
    next if freqs[n].zero?

    freqs[n] -= 1
    if terminates[n - 1] > 0
      terminates[n - 1] -= 1
      terminates[n] += 1
    elsif freqs[n + 1] > 0 && freqs[n + 2] > 0
      freqs[n + 1] -= 1
      freqs[n + 2] -= 1
      terminates[n + 2] += 1
    else
      return false
    end
  end
  true
end

nums = [1, 2, 3, 3, 4, 4, 5, 5]
nums = [1, 2, 3, 3, 4, 5]
# require 'random'
# nums = 100000.times.map {Random.rand(10)}
# p nums
p is_possible(nums)
