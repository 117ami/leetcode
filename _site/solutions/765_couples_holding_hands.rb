#
# N couples sit in 2N seats arranged in a row and want to hold hands.  We want to know the minimum number of swaps so that every couple is sitting side by side.  A swap consists of choosing any two people, then they stand up and switch seats.
# The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.
# Example 1:
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
# Example 2:
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# Note:
#
#  len(row) is even and in the range of [4, 60].
#  row is guaranteed to be a permutation of 0...len(row)-1.
#
#  https://leetcode.com/problems/couples-holding-hands/description/
require './aux.rb'

# @param {Integer[]} row
# @return {Integer}
def min_swaps_couples(row)
  return 0 if row.size < 3
  amap = Hash.new(0).tap { |h| row.each_with_index { |n, idx| h[n] = idx } }
  res = 0

  (0..row.size - 2).step(2).each do |i|
    next if pair?(row[i..i + 1])
    curval = row[i]
    nxtval = row[i + 1]
    pairval = curval.even? ? curval + 1 : curval - 1
    pairid = amap[pairval]
    strangerid = i + 1

    until pair?([curval, nxtval])
      row[pairid], row[strangerid] = row[strangerid], row[pairid]
      strangerid = pairid.even? ? pairid + 1 : pairid - 1
      curval = nxtval
      pairval = curval.even? ? curval + 1 : curval - 1
      pairid = amap[pairval]
      nxtval = row[strangerid]
      res += 1
    end
  end
  res
end

def pair?(arr)
  return true if arr[0].even? && arr[1] == arr[0] + 1 || arr[0].odd? && arr[1] == arr[0] - 1
  false
end

row = Array(1..6).shuffle
row = [4, 5, 1, 2, 3, 6]
row = [0, 2, 4, 6, 7, 1, 3, 5]
row = [0, 2, 1, 3]
p row
p min_swaps_couples(row)
