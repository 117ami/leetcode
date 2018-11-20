# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
# Example:
# 16 true
# 14 false

# @param {Integer} num
# @return {Boolean}
def is_perfect_square(num)
  (1..num / 2 + 2).step(3) do |i|
    if i * i == num
      return true
    elsif i * i > num
      return true if (i - 1) * (i - 1) == num ||
                     (i - 2) * (i - 2) == num
      break
    end
  end
  false
end

def is_perfect_square2(num)
  low = 1
  high = num
  while low <= high
    mid = (low + high) / 2
    if mid * mid < num
      low = mid + 1
    elsif mid * mid > num
      high = mid - 1
    else
      return true
    end
  end
  false
end

p is_perfect_square(10)
p is_perfect_square(2_147_483_647)
p is_perfect_square2(2_147_483_647)

(1..200).each do |i|
  p i if is_perfect_square(i)
  p i if is_perfect_square2(i)
end
