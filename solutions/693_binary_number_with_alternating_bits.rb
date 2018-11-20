# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
# @param {Integer} n
# @return {Boolean}
def has_alternating_bits(n)
  prev = 0
  n.to_s(2).each_char do |b|
    return false if b == prev
    prev = b
  end
  true
end

def has_alternating_bits2(n)
  p n.to_s(2)
  !n.to_s(2).scan(/^(10)*1?$/).empty?
end

n = 10
p has_alternating_bits(n)
p has_alternating_bits2(n)
