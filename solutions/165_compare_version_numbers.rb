# Compare two version numbers version1 and version2.
# If version1 &gt; version2 return 1;&nbsp;if version1 &lt; version2 return -1;otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not &quot;two and a half&quot; or &quot;half way to version three&quot;, it is the fifth second-level revision of the second first-level revision.
# Example 1:
# Input: version1 = &quot;0.1&quot;, version2 = &quot;1.1&quot;
# Output: -1
# Example 2:
# Input: version1 = &quot;1.0.1&quot;, version2 = &quot;1&quot;
# Output: 1
# Example 3:
# Input: version1 = &quot;7.5.2.4&quot;, version2 = &quot;7.5.3&quot;
# Output: -1
#

# @param {String} version1
# @param {String} version2
# @return {Integer}
def compare_version(version1, version2)
  va, vb = [version1, version2].map { |v| v.split('.').map(&:to_i) }
  xsize = [va.size, vb.size].max
  va.concat([0] * 100)
  vb.concat([0] * 100)
  0.upto(xsize - 1) do |i|
    return -1 if va[i] < vb[i]
    return 1 if va[i] > vb[i]
  end
  0
end

version1 = '7.5.2.4'
version2 = '7.5.3'
version1 = '19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0'
version2 = '19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000'
p compare_version(version1, version2)
