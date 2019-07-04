# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example 1:
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

# @param {Integer} numerator
# @param {Integer} denominator
# @return {String}
def fraction_to_decimal(numerator, denominator)
  return '0' if numerator.zero?
  res = []
  remainder = {}
  insertdot = false
  negres = false
  if numerator < 0 || denominator < 0
    negres = true if numerator * denominator < 0
    numerator = numerator.abs
    denominator = denominator.abs
  end

  loop do
    if numerator < denominator && !insertdot
      res << '.'
      insertdot = true
    end

    i = -1
    while numerator < denominator
      remainder[numerator] = nil
      numerator *= 10
      i += 1
      res << 0 if i > 0
    end

    quo = numerator / denominator
    numerator = numerator % denominator
    res << quo

    break if remainder.key?(numerator) || numerator.zero?
    remainder[numerator] = quo
  end

  res.unshift(0) if res[0] == '.'
  res.unshift('-') if negres
  return res.join if remainder.empty? || numerator.zero? # not a circulating decimal
  ks = remainder.keys
  ks.shift until ks[0] == numerator
  res.insert(res.size - ks.size, '(')
  res << ')'
  res.join
end

numerator = -22
denominator = -2
p numerator * 1.0 / denominator
p fraction_to_decimal(numerator, denominator)
