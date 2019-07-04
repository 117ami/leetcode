# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# @param {Integer} c
# @return {Boolean}
def judge_square_sum(c)
  return true if c.zero?
  (1..Math.sqrt(c).floor).each do |a|
    b = Math.sqrt(c - a**2)
    return true if (b - b.floor).zero?
  end
  false
end

def judge_square_sum2(c)
  left = 0
  right = Math.sqrt(c).floor
  while left <= right
    res = left**2 + right**2
    if res < c
      left += 1
    elsif res > c
      right -= 1
    else
      return true
    end
  end
  false
end

c = 2
p judge_square_sum(c)
p judge_square_sum2(c)
