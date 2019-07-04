# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
#
#     If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#     For example, the word 'apple' becomes 'applema'.
#
#     If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
#     For example, the word "goat" becomes "oatgma".
#
#     Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#     For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
#
# Return the final sentence representing the conversion from S to Goat Latin.

# @param {String} s
# @return {String}
def to_goat_latin(s)
  arr = s.split(' ')
  (0..arr.size - 1).each do |i|
    arr[i] = arr[i][1..-1] + arr[i][0] unless arr[i][0] =~ /[aeiou]/i
    arr[i] << 'ma' + 'a' * (i + 1)
  end
  arr.join
end

s = 'I Speak Goat Latin'
s = 'The quick brown fox jumped over the lazy dog'
p to_goat_latin(s)
