#include "aux.cpp"
/**
Write a program to find the node at which the intersection of two singly linked
lists begins.
For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function
returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:Special thanks to @stellari for adding this problem and creating all
test cases.
 https://leetcode.com/problems/intersection-of-two-linked-lists/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
  ListNode *getIntersectionNode(ListNode *ha, ListNode *hb) {
    if (ha == nullptr || hb == nullptr)
      return nullptr;
    ListNode *pa = ha;
    ListNode *pb = hb;
    while (pa != NULL && pb != nullptr && pa != pb) {
      pa = pa->next;
      pb = pb->next;
      if (pa == pb)
        return pa;

      if (pa == NULL)
        pa = hb;
      if (pb == NULL)
        pb = ha;
    }
    return pa;
  }
};

int main() {
  Solution s;
  ListNode *ha = new ListNode(1);
  ListNode *hb = new ListNode(6);
}
