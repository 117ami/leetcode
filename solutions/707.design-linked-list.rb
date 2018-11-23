# require './aux.rb'
class MyLinkedList
  #     Initialize your data structure here.
  def initialize
    @list = []
  end

  #     Get the value of the index-th node in the linked list. If the index is invalid, return -1.
  #     :type index: Integer
  #     :rtype: Integer
  def get(index)
    @list[index] || -1
  end

  #     Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
  #     :type val: Integer
  #     :rtype: Void
  def add_at_head(val)
    @list.unshift(val)
  end

  #     Append a node of value val to the last element of the linked list.
  #     :type val: Integer
  #     :rtype: Void
  def add_at_tail(val)
    @list << val
  end

  #     Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
  #     :type index: Integer
  #     :type val: Integer
  #     :rtype: Void
  def add_at_index(index, val)
    return if index > @list.size 
    @list.insert(index, val)
  end

  #     Delete the index-th node in the linked list, if the index is valid.
  #     :type index: Integer
  #     :rtype: Void
  def delete_at_index(index)
    @list.delete_at(index)
  end
end
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList.new
p obj.get(0)
obj.add_at_head(2)
obj.add_at_tail(3)
obj.add_at_index(1, 4)
obj.delete_at_index(9)
p obj.get(2)
# [707] Design Linked List
# https://leetcode.com/problems/design-linked-list/description/
# * algorithms
# * Easy (19.46%)
# * Total Accepted:    11.4K
# * Total Submissions: 58.8K
# * Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
# Implement these functions in your linked list class:
#   get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#   addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#   addAtTail(val) : Append a node of value val to the last element of the linked list.
#   addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#   deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
# Example:
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# Note:
#   All values will be in the range of [1, 1000].
#   The number of operations will be in the range of [1, 1000].
#   Please do not use the built-in LinkedList library.
