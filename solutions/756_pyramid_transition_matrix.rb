#
# We are stacking blocks to form a pyramid.  Each block has a color which is a one letter string, like `'Z'`.
# For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`.  We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
# We start with a bottom row of bottom, represented as a single string.  We also start with a list of allowed triples allowed.  Each allowed triple is represented as a string of length 3.
# Return true if we can build the pyramid all the way to the top, otherwise false.
# Example 1:
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   D   E
#  / \ / \
# X   Y   Z
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
# Example 2:
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
# Note:
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
#
#  https://leetcode.com/problems/pyramid-transition-matrix/description/
require './aux.rb'

# @param {String} bottom
# @param {String[]} allowed
# @return {Boolean}

def pyramid_transition(bottom, allowed)
  return false if allowed.empty?
  triples = Hash.new([]).tap { |h| allowed.each { |s| (h[s[0..1]] |= []) << s[2] } }
  p triples

  dp = Array.new(bottom.size) { Array.new(bottom.size) { [] } }
  0.upto(bottom.size - 1).each { |i| dp[0][i] = [bottom[i]] }
  1.upto(bottom.size - 1).each do |level|
    0.upto(bottom.size - 1 - level).each do |slot|
      dp[level][slot] = dp[level - 1][slot].product(dp[level - 1][slot + 1]).map { |a| triples[a.join] }.flatten.compact.uniq
      return false if dp[level][slot].empty?
    end
  end
  # p dp
  true
end

bottom = 'XXXZ'
allowed = %w[XXX XXY XYX XYY YXZ]
bottom = 'CBDDA'
allowed = %w[ACC ACA AAB BCA BCB BAC BAA CAC BDA CAA CCA CCC CCB DAD CCD DAB ACD DCA CAD CBB ABB ABC ABD BDB BBC BBA DDA CDD CBC CBA CDA DBA ABA]

p pyramid_transition(bottom, allowed)

