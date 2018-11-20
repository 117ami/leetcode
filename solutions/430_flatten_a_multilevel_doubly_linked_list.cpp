#include "aux.cpp"
/**
You are given a doubly linked list which in addition to the next and previous
pointers, it could have a child pointer, which may or may not point to a
separate doubly linked list. These child lists may have one or more children of
their own, and so on, to produce a multilevel data structure, as shown in the
example below. Flatten the list so that all the nodes appear in a single-level,
doubly linked list. You are given the head of the first level of the list.

Example:
Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

Explanation for the above example:
Given the following multilevel doubly linked list:

We should return the following flattened doubly linked list:

 https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Node {
public:
  int val = 0;
  Node *prev = NULL;
  Node *next = NULL;
  Node *child = NULL;

  Node() {}

  Node(int _val, Node *_prev, Node *_next, Node *_child) {
    val = _val;
    prev = _prev;
    next = _next;
    child = _child;
  }
};

class Solution {
public:
  Node *flatten(Node *head) {
    if (head == nullptr || (nullptr == head->next && nullptr == head->child))
      return head;
    if (head->next && !head->child) {
      Node *tmp = flatten(head->next);
      head->next = tmp;
      tmp->prev = head;
    } else if (head->child && !head->next) {
      Node *tmp = flatten(head->child);
      head->next = tmp;
      tmp->prev = head;
      // DONT forget to nullify the child branch  
      head->child=NULL; 
    } else {
      Node *tmp = flatten(head->child);
      Node *tmp2 = flatten(head->next);
      head->next = tmp;
      tmp->prev = head;
      head->child=NULL; 
      while (tmp->next)
        tmp = tmp->next;
      tmp->next = tmp2;
      tmp2->prev = tmp;
    }
    return head;
  }
};

int main() { Solution s; }
