
#include "aux.cpp"
#include "445.add-two-numbers-ii.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi a = {7, 2,4,3}, b = {5,6,4};
	a = {5}, b = {5};
	vi d = s.addTwoVector(a, b);
	say(d);
	ListNode* l1 = arrayToListNode(a); 
	ListNode* l2 = arrayToListNode(b); 
	ListNode* res = s.addTwoNumbers(l1, l2); 
	vi c = listnodeToArray(res);
	say(c);
	return 0;
}

