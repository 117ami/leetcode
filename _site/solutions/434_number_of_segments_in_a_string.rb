=begin
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5

=end

# @param {String} s
# @return {Integer}
def count_segments(s)
	s.split().size	
end

s = " hello, my anme is      skdljf   "

p count_segments(s)