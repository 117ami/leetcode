# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_grammar(n, k)
  return 0 if n == 1
  k > 2**(n - 2) ? 1 - kth_grammar(n - 1, k - 2**(n - 2)) : kth_grammar(n - 1, k)
end

n = 5
1.upto(16).each do |k|
  print kth_grammar(n, k)
end

puts 
puts 5 ^ 2