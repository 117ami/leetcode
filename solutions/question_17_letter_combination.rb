
# Letter combinations of a phone number
# Given a digit string, return all possible letter
#  combinations that the number could represent.

# @param {String} digits
# @return {String[]}

def initcache
  letters = Array('a'..'z')
  cache = Hash[(2..7).map { |i| [i, letters[(i - 2) * 3..(i - 2) * 3 + 2]] }]
  cache[7].push('s')
  cache[8] = %w[t u v]
  cache[9] = %w[w x y z]
  cache
end

def letter_combinations(digits)
  cache = initcache
  digits.tr!('1', '')
  return [] if digits.empty?
  res = ['']

  digits.each_char do |d|
    res = res.product(cache[d.to_i]).map! { |v| v.join('') }
  end
  res
end

p letter_combinations('2323')
