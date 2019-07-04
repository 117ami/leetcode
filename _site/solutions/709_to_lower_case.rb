=begin
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"
Example 2:
Input: "here"
Output: "here"
Example 3:
Input: "LOVELY"
Output: "lovely"

 https://leetcode.com/problems/to-lower-case/description/ 
=end

# @param {String} str
# @return {String}
def to_lower_case(str)
   str.downcase 
end

str = "HERE"
p to_lower_case(str)