# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.

# @param {String} s
# @return {Integer[]}
def partition_labels(s)
  h = {}
  r = [[0, 0]]
  s.each_char.with_index do |c, i|
    h[c] = [i, i] unless h.key?(c)
    h[c][-1] = i
  end
  n = h.values.sort_by(&:first)
  until n.empty?
    cur = n.shift
    if r[-1][0] > cur[1] || r[-1][1] < cur[0]
      r << cur
    else
      r[-1][0] = [r[-1][0], cur[0]].min
      r[-1][1] = [r[-1][1], cur[1]].max
    end
  end
  r.map { |v| v[-1] - v[0] + 1 }
end

s = 'ababcbacadefegdehijhklij'
p partition_labels(s)
