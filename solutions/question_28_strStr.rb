
# Implement strStr(): Return the index of the first occurrence of needle in
#  haystack, or -1 if needle is not part of haystack.

# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  haystack =~ /#{needle}/ || -1
  # or haystack.index(needle) ||= -1
end

p str_str('hello', 'aa')
