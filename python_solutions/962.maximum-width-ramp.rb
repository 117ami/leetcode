# @param {Integer[]} a
# @return {Integer}
def max_width_ramp(a)
  res = 0
  stack = []
  (a.size - 1).downto(0).each do |i|
    if stack.empty? || a[i] > stack.last.first
      stack << [a[i], i]
    else
      j = (0..stack.size - 1).bsearch { |idx| a[i] <= stack[idx].first }
      res = [res, stack[j].last - i].max
  end
  end
  res
end

a = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
# a = [6, 0, 8, 2, 1, 5]
p max_width_ramp(a)
