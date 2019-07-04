# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

# @param {String} s
# @return {String[]}
def restore_ip_addresses(s)
  res = split_string(s, 4).keep_if { |i| i.size == 4 }.map { |i| i.join('.') }
end

def split_string(s, k)
  return [[]] if s.nil? || s.size < k
  if k == 1
    return [[]] if s.size > 1 && s[0] == '0' || s.to_i > 255
    return [[s]]
  end

  ans = []
  (0..2).each do |i|
    a = s[0..i]
    return ans if a.size > 1 && a[0] == '0' || a.to_i > 255 # no more valid ones
    split_string(s[i + 1..-1], k - 1).each { |res| ans << [a].concat(res) }
  end
  ans
end

s = '25525511135'
s = '010010'
p restore_ip_addresses(s)
