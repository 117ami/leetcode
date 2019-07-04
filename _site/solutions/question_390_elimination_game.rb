
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
#
# Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6

# @param {Integer} n
# @return {Integer}
def last_remaining(n)
  head = 1
  remain = n
  left_2right = true
  round = 0
  while remain > 1
    head += 2**round if left_2right || remain.odd?
    left_2right = !left_2right
    round += 1
    remain /= 2
  end
  head
end

n = 12
last_remaining(n)
