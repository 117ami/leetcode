#
# @lc app=leetcode id=1054 lang=ruby
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (32.68%)
# Total Accepted:    2.8K
# Total Submissions: 7.8K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
#
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
#
#
#
# Example 1:
#
#
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
#
#
#
#
# Note:
#
#
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
#
#
#
#
#
#
# @param {Integer[]} barcodes
# @return {Integer[]}
def rearrange_barcodes(barcodes)
  return barcodes if barcodes.size < 3

  res = [0] * barcodes.size
  freq = Hash.new(0).tap { |h| barcodes.each { |b| h[b] += 1 } }
  i = 0
  freq.sort_by { |_, v| -v }.each do |k, v|
    v.times do
      res[i] = k
      i += 2
      i = 1 if i >= res.size
    end
  end
  res
end

# require './aux.rb'
# barcodes = random_list(20, 5)
# barcodes = [2, 1, 1]
# barcodes = [7, 7, 7, 8, 5, 7, 5, 5, 5, 8]
# p barcodes
# p rearrange_barcodes(barcodes)
