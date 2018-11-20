# In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietnes
# }
#
# For convenience, we'll call the person with label x, simply "person x".
#
# We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.
#
# Also, we'll say quiet[x] = q if person x has quietness q.
#
# Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.
#
# Example 1:
#
# Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
# Explanation:
# answer[0] = 5.
# Person 5 has more money than 3, which has more money than 1, which has more money than 0.
# The only person who is quieter (has lower quiet[x]) is person 7, but
# it isn't clear if they have more money than person 0.
#
# answer[7] = 7.
# There isn't anyone who definitely has more money than person 7, so the person who definitely has
# equal to or more money than person 7 is just person 7.
#
# The other answers can be filled out with similar reasoning.
# Note:
#
# 1 <= quiet.length = N <= 500
# 0 <= quiet[i] < N, all quiet[i] are different.
# 0 <= richer.length <= N * (N-1) / 2
# 0 <= richer[i][j] < N
# richer[i][0] != richer[i][1]
# richer[i]'s are all different.
# The observations in richer are all logically consistent.

# @param {Integer[][]} richer
# @param {Integer[]} quiet
# @return {Integer[]}
def loud_and_rich(richer, quiet)
  rtm = {} # rtm: richer than me
  richer.each do |pair|
    rtm[pair[1]] = [] unless rtm.key?(pair[1])
    rtm[pair[1]] << pair[0]
  end
  quiet = Array(0..quiet.size - 1).zip(quiet).to_h
  res = []
  (0..quiet.size - 1).each do |i|
    res[i] = i
    minv = quiet[i]
    todo = rtm[i].dup || []
    qvalues = {}
    until todo.empty?
      curman = todo.shift
      next if qvalues.key?(curman)
      qvalues[curman] = quiet[curman]
      todo = todo.concat(rtm[curman]) if rtm.key?(curman)
    end
    qvalues.each do |k, v|
      if v < minv
        res[i] = k
        minv = v
      end
    end
  end
  res
end
