#
# Implement a MapSum class with insert, and sum methods.
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#
#  https://leetcode.com/problems/map-sum-pairs/description/
require './aux.rb'

class MapSum
  #     Initialize your data structure here.
  def initialize
    @hash = {}
  end

  #     :type key: String
  #     :type val: Integer
  #     :rtype: Void
  def insert(key, val)
    @hash[key] = val
  end

  #     :type prefix: String
  #     :rtype: Integer
  def sum(prefix)
    res = 0
    @hash.keys.each do |k|
      next if k.scan(/^#{prefix}/).empty?
      res += @hash[k]
    end
    res
  end
end

# Your MapSum object will be instantiated and called as such:
obj = MapSum.new
obj.insert('apple', 3)
p obj.sum('ap')
obj.insert('app', 2)
p obj.sum('ap')
# param_2 = obj.sum(prefix)
