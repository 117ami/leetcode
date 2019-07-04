# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

# @param {String} s
# @return {Integer}
def title_to_number(s)
  mmp = Array('A'..'Z').zip(1..26).to_h
  s.each_char.reduce(0) {|sum, c| sum *= 26; sum += mmp[c]}
end

p title_to_number('ZY')
p 'AB'.to_i(26)
