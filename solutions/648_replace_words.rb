#
# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
# You need to output the sentence after the replacement.
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Note:
# The input will only have lower-case letters.
#  1 <= dict words number <= 1000
#  1 <= sentence words number <= 1000
#  1 <= root length <= 100
#  1 <= sentence words length <= 1000
#
#  https://leetcode.com/problems/replace-words/description/
require './aux.rb'

# @param {String[]} dict
# @param {String} sentence
# @return {String}
def replace_words(dict, sentence)
  res = []
  roots = dict.zip([nil]).to_h
  sentence.split(/\s/).each do |w|
    matched = false
    0.upto(w.size - 1).each do |idx|
      next unless roots.key?(w[0..idx])
      res << w[0..idx]
      matched = true
      break
    end
    res << w unless matched
  end
  res.join(' ')
end

dict = %w[cat bat rat]
sentence = 'the cattle was rattled by the abattery'
p replace_words(dict, sentence)
