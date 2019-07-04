#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Reverse a linked list from position m to n. Do it in one-pass.
Note:1 <= m <= n <= length of list.
Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

 **/
using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  ListNode *reverseBetween(ListNode *head, int m, int n) {
    ListNode *newhead = new ListNode(0);
    newhead->next = head;
    ListNode *dummy = head;
    for (int i = 0; i < m - 1; i++)
      dummy = dummy->next;
    ListNode *cur = dummy->next;
    for (int i = 0; i < n - m; i++) {
      ListNode *tmp = cur->next;
      cur->next = tmp->next;
      tmp->next = dummy->next;
      dummy->next = tmp;
    }
    return newhead->next;
  }
};

int main() { Solution s; }
