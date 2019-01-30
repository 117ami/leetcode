
# @param {Integer} a
# @param {Integer} b
# @return {String}
def str_without3a3b(a, b)
   return 'a' * a if b.zero?
   return 'b' * b if a.zero?
   return 'ab' * a if a == b
   return 'aab' + str_without3a3b(a-2, b-1) if a > b
   str_without3a3b(a-1, b-2) + 'abb'
end