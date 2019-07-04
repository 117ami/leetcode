# Koko loves to eat bananas. There are Npiles of bananas, the i-thpile has piles[i] bananas. The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile. If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.
#
# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
#
# Note:
#   1 <= piles.length <= 10^4
#   piles.length <= H <= 10^9
#   1 <= piles[i] <= 10^9
#
#  https://leetcode.com/problems/koko-eating-bananas/description/

# @param {Integer[]} piles
# @param {Integer} h
# @return {Integer}
def min_eating_speed(piles, h)
  return piles.max if h == piles.size
  low = 1
  high = piles.max
  res = (low + high) / 2
  while low < high
  	tmp = 0
  	p [low, res, high]
    piles.each do |ppp|
      tmp += (ppp * 1.0 / res).ceil
    end
    if tmp > h
      low = res + 1
    else
      high = res
    end
    res = (high + low) / 2
  end

  res
end

piles = [3, 6, 7, 11]
h = 8
piles = [30, 11, 23, 4, 20]
h = 6
piles = [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184]
h = 823855818
p min_eating_speed(piles, h)
