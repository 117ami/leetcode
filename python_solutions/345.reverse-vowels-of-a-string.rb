# @param {String} s
# @return {String}
def reverse_vowels(s)
  vowels = s.scan(/[aeiou]/i)
  s.gsub(/[aeiou]/i) { vowels.pop }
end

s = 'hello'
p reverse_vowels(s)
