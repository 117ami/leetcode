
#include "aux.cpp"
#include "c.cpp"
#include "987.vertical-order-traversal-of-a-binary-tree.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr ={3,9,20,INT_MIN,INT_MIN,15,7};
	arr = {1,2,3,4,5,6,7};
	TreeNode* r = growTreeFromList(arr);
	vvi res = s.verticalTraversal(r);
	say(res);
	return 0;
}

