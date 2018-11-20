=begin
Design a HashMapwithout using any built-in hash table libraries.
To be specific, your design should include these functions:
	put(key, value) :Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
	get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
	remove(key) :Remove the mapping for the value key if this map contains the mapping for the key.
Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);     
hashMap.put(2, 2);     
hashMap.get(1);      // returns 1
hashMap.get(3);      // returns -1 (not found)
hashMap.put(2, 1);     // update the existing value
hashMap.get(2);      // returns 1 
hashMap.remove(2);     // remove the mapping for 2
hashMap.get(2);      // returns -1 (not found) 
Note:
	All keys and values will be in the range of [0, 1000000].
	The number of operations will be in the range of[1, 10000].
	Please do not use the built-in HashMap library.

 https://leetcode.com/problems/design-hashmap/description/ 
=end
require './aux.rb'

class MyHashMap

=begin
    Initialize your data structure here.
=end
    def initialize()
    	@arr = []
    	10003.times {@arr << [nil, -1]}
    end


=begin
    value will always be non-negative.
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
    	xk = key % 10001 
        xk = (xk + 1) % 10001 while @arr[xk].first != nil && @arr[xk].first != key 
        @arr[xk] = [key, value] 
    end


=begin
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
    	xk = key % 10001 
    	theend = (xk + 10000) % 10001
        xk = (xk + 1) % 10001 while @arr[xk].first != key && xk != theend
        return @arr[xk].last if @arr[xk].first == key
        -1
    end


=begin
    Removes the mapping of the specified value key if this map contains a mapping for the key
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
    	xk = key % 10001 
        xk = (xk + 1) % 10001 while @arr[xk].first != nil && @arr[xk].first != key 
        @arr[xk] = [nil, -1] if @arr[xk].first == key
    end


end

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap.new()
obj.put(100023, 12)
obj.put(1000203, 18)
param_2 = obj.get(100023)
p param_2
p obj.get(1000203)
obj.remove(100023)