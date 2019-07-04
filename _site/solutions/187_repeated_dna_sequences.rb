=begin
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

 https://leetcode.com/problems/repeated-dna-sequences/description/ 
=end
require './aux.rb'

# @param {String} s
# @return {String[]}
def find_repeated_dna_sequences(s)
   return [] if s.length < 11
   freq = Hash.new(0)
   (0..s.size-10).each {|i| freq[s[i..i+9]] += 1}
   freq.keys.keep_if{|k| freq[k] > 1}
end
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
p find_repeated_dna_sequences(s)