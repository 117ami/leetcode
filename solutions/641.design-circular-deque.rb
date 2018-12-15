# require './aux.rb'
class MyCircularDeque
  #     Initialize your data structure here. Set the size of the deque to be k.
  #     :type k: Integer
  def initialize(k)
    @arr = []
    @size = k
  end

  #     Adds an item at the front of Deque. Return true if the operation is successful.
  #     :type value: Integer
  #     :rtype: Boolean
  def insert_front(value)
    return false if @arr.size == @size

    @arr.unshift(value)
    true
  end

  #     Adds an item at the rear of Deque. Return true if the operation is successful.
  #     :type value: Integer
  #     :rtype: Boolean
  def insert_last(value)
    return false if @arr.size == @size
    @arr << value
    true
  end

  #     Deletes an item from the front of Deque. Return true if the operation is successful.
  #     :rtype: Boolean
  def delete_front
    return false if @arr.empty?

    @arr.shift
    true
  end

  #     Deletes an item from the rear of Deque. Return true if the operation is successful.
  #     :rtype: Boolean
  def delete_last
    return false if @arr.empty?

    @arr.pop
    true
  end

  #     Get the front item from the deque.
  #     :rtype: Integer
  def get_front
    return -1 if @arr.empty?

    @arr[0]
  end

  #     Get the last item from the deque.
  #     :rtype: Integer
  def get_rear
    return -1 if @arr.empty?

    @arr.last
  end

  #     Checks whether the circular deque is empty or not.
  #     :rtype: Boolean
  def is_empty
    @arr.empty?
  end

  #     Checks whether the circular deque is full or not.
  #     :rtype: Boolean
  def is_full
    @arr.size = @size
  end
end
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque.new(k)
# param_1 = obj.insert_front(value)
# param_2 = obj.insert_last(value)
# param_3 = obj.delete_front()
# param_4 = obj.delete_last()
# param_5 = obj.get_front()
# param_6 = obj.get_rear()
# param_7 = obj.is_empty()
# param_8 = obj.is_full()
# [641] Design Circular Deque
# https://leetcode.com/problems/design-circular-deque/description/
# * algorithms
# * Medium (48.42%)
# * Total Accepted:    3.6K
# * Total Submissions: 7.3K
# * Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
# Design your implementation of the circular double-ended queue (deque).
# Your implementation should support following operations:
#   MyCircularDeque(k): Constructor, set the size of the deque to be k.
#   insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
#   insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
#   deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
#   deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
#   getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
#   getRear(): Gets the last item from Deque. If the deque is empty, return -1.
#   isEmpty(): Checks whether Deque is empty or not. 
#   isFull(): Checks whether Deque is full or not.
# Example:
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
# circularDeque.insertLast(1);      // return true
# circularDeque.insertLast(2);      // return true
# circularDeque.insertFront(3);      // return true
# circularDeque.insertFront(4);      // return false, the queue is full
# circularDeque.getRear();        // return 2
# circularDeque.isFull();        // return true
# circularDeque.deleteLast();      // return true
# circularDeque.insertFront(4);      // return true
# circularDeque.getFront();      // return 4
# Note:
#   All values will be in the range of [0, 1000].
#   The number of operations will be in the range of [1, 1000].
#   Please do not use the built-in Deque library.
