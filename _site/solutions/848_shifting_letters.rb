# We have a string S of lowercase letters, and an integer array shifts.
#
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
#
# Return the final string after all such shifts to S are applied.
#
# Example 1:
#
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation:
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
# Note:
#
# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9

# @param {String} s
# @param {Integer[]} shifts
# @return {String}
def shifting_letters(s, shifts)
  num2letter = Array(0..25).zip(Array('a'..'z')).to_h
  letters2num = num2letter.invert
  (0..shifts.size - 2).reverse_each do |i|
    shifts[i] += shifts[i + 1]
  end

  shifts.each_with_index do |n, i|
    s[i] = num2letter[(letters2num[s[i]] + n) % 26]
  end
  s
end

s = 'abc'
shifts = [3, 5, 9]
p shifting_letters(s, shifts)
