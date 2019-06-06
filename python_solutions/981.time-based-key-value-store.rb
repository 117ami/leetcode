#
# @lc app=leetcode id=981 lang=ruby
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (50.64%)
# Total Accepted:    12.1K
# Total Submissions: 23.9K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' + '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Create a timebased key-value store class TimeMap, that supports two
# operations.
#
# 1. set(string key, string value, int timestamp)
#
#
# Stores the key and value, along with the given timestamp.
#
#
# 2. get(string key, int timestamp)
#
#
# Returns a value such that set(key, value, timestamp_prev) was called
# previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest
# timestamp_prev.
# If there are no values, it returns the empty string ("").
#
#
#
#
#
# Example 1:
#
#
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs =
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:  
# TimeMap kv;  
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with
# timestamp = 1  
# kv.get("foo", 1);  // output "bar"  
# kv.get("foo", 3); // output "bar" since there is no value corresponding to
# foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie
# "bar"  
# kv.set("foo", "bar2", 4);  
# kv.get("foo", 4); // output "bar2"  
# kv.get("foo", 5); //output "bar2"  
#
#
#
#
# Example 2:
#
#
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs
# =
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]
#
#
#
#
#
#
# Note:
#
#
# All key/value strings are lowercase.
# All key/value strings have length in the range [1, 100]
# The timestamps for all TimeMap.set operations are strictly increasing.
# 1 <= timestamp <= 10^7
# TimeMap.set and TimeMap.get functions will be called a total of 120000 times
# (combined) per test case.
#
#
#
# A native Priority Queue
class PriorityQueue
  def elements
    @es
  end

  def initialize
    @es = []
  end

  def empty?
    @es.empty?
  end

  def size
    @es.size
  end

  def <<(x)
    push(x)
  end

  def shift
    @es.shift
  end

  def pop
    @es.pop
  end

  def push(x) # x is assumed to be an integer or a string
    return pusharray(x) if x.is_a?(Array)

    idx = (0..@es.size - 1).bsearch { |i| @es[i] < x } || @es.size
    @es.insert(idx, x)
  end

  def pusharray(x) # x is assumed to be an array
    idx = (0..@es.size - 1).bsearch { |i| @es[i].first <= x.first } || @es.size
    @es.insert(idx, x)
  end
end

class TimeMap
  #     Initialize your data structure here.
  def initialize
    @values = Hash.new { |h, k| h[k] = [] }
    @stamps = Hash.new { |h, k| h[k] = [] }
  end

  #     :type key: String
  #     :type value: String
  #     :type timestamp: Integer
  #     :rtype: Void
  def set(key, value, timestamp)
    @values[key] << value
    @stamps[key] << timestamp
  end

  #     :type key: String
  #     :type timestamp: Integer
  #     :rtype: String
  def get(key, timestamp)
    return '' if @values[key].empty?

    ts = @stamps[key]
    idx = (0..ts.size - 1).bsearch { |i| ts[i] > timestamp } || ts.size
    return '' if idx.zero?

    @values[key][idx - 1]
  end
end

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap.new
obj.set('love', 'high', 10)
obj.set('love', 'low', 20)
p obj.get('love', 5)
p obj.get('love', 10)
p obj.get('love', 15)
p obj.get('love', 20)
p obj.get('love', 25)
