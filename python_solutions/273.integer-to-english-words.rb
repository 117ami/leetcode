#
# @lc app=leetcode id=273 lang=ruby
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (24.20%)
# Total Accepted:    100K
# Total Submissions: 413K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
#
# Example 4:
#
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
#
#
#
# @param {Integer} num
# @return {String}
def number_to_words(num)
  return 'Zero' if num.zero?

  below19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split
  tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split
  ks = 'Thousand Million Billion'.split
  words = lambda do |n, k|
  	return [] if n.zero?
    return [below19[n - 1]] if n <= 19
    return [tens[n / 10 - 2]] + words.call(n % 10, k) if n <= 99
    return [below19[n / 100 - 1]] + ['Hundred'] + words.call(n % 100, k) if n < 1000

    m = n / 1000
    r = n % 1000
    space = m % 1000 == 0 ? [] : [ks[k]]
    return words.call(m, k + 1) + space + words.call(r, k)
  end
  words.call(num, 0).join(' ')
end

p number_to_words(20)
