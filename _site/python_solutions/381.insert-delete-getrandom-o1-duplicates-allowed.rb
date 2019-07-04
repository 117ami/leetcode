#
# @lc app=leetcode id=381 lang=ruby
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (30.93%)
# Total Accepted:    35K
# Total Submissions: 113K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
#
#
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
#
#
#
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
#
#
#
class RandomizedCollection
  #     Initialize your data structure here.
  def initialize
    @pos = {}
    @num = []
  end

  #     Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
  #     :type val: Integer
  #     :rtype: Boolean
  def insert(val)
    res = true
    res = false if @pos.key?(val)
    @pos[val] = [] unless @pos.key?(val)
    @pos[val] << @num.size
    @num << [val, @pos[val].size - 1]
    res
  end

  #     Removes a value from the collection. Returns true if the collection contained the specified element.
  #     :type val: Integer
  #     :rtype: Boolean
  def remove(val)
    return false if @pos.empty? || !@pos.key?(val)

    lastval, lastidx = @num.last
    @pos[lastval][lastidx] = @pos[val].last
    @num[@pos[val].last] = @num.last
    @num.pop
    @pos[val].pop
    @pos.delete(val) if @pos[val] == []
    true
  end

  #     Get a random element from the collection.
  #     :rtype: Integer
  def get_random
    @num.sample.first
  end
end

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection.new()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.get_random()
