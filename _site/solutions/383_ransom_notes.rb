#  Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
  a = ransom_note.chars.group_by(&:itself)
  b = magazine.chars.group_by(&:itself)
  a.each_pair do |k, v|
    return false if !b.key?(k) || b[k].size < v.size
  end
  true
end

def can_construct2(ransom_note, magazine)
  a = ransom_note.chars.sort
  b = magazine.chars.sort
  i = j = 0
  while i < a.size
    i += 1 if a[i] == b[j]
    j += 1
    return false if j >= b.size && i < a.size
  end
  true
end

def can_construct3(ransom_note, magazine)
  ransom_note.each_char do |c|
    return false unless magazine.include?(c)
    magazine.slice!(c)
  end
  true
end

sr = 'djfjfhjf'
sm = 'aaigcbiafifghhdihcfdjjej'
# sm = 'aabbbcc'
p can_construct(sr, sm)
p can_construct2(sr, sm)
p can_construct3(sr, sm)
