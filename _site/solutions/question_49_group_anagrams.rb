
# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.

# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
  return [] if strs.empty?
  ana = Hash.new { |hash, k| hash[k] = [] }
  strs.each do |c|
    ana[c.chars.sort.join] << c
  end
  ana.values
end

strs = %w[cab tin pew duh may ill buy bar max doc]
# strs = %w[eat tea tan ate nat bat]
p group_anagrams(strs)
