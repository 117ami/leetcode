
# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.
#
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
#
# Return the smallest possible value of D.
#
# Example:
#
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# Note:
#
# stations.length will be an integer in range [10, 2000].
# stations[i] will be an integer in range [0, 10^8].
# K will be an integer in range [1, 10^6].
# Answers within 10^-6 of the true value will be accepted as correct.
def minmax_gas_dist(sta, k)
  return 0 if sta.size < 2
  sta.sort!
  low = 0
  high = sta[-1] + 1

  while high - low > 10**-6
    # print " high : #{high} low #{low} \n"
    mid = (high + low) / 2.0
    sum = 0
    0.upto(sta.size - 2).each do |i|
      sum += ((sta[i + 1] - sta[i]) / mid - 1).ceil
    end
    sum <= k ? high = mid : low = mid
  end
  low
end

sta = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98]
# sta = Array(1..10) # [1, 6, 8, 9, 13, 17, 27] # Array.new(10, rand(30))
k = 1
p minmax_gas_dist(sta, k)
