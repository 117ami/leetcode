
#include "aux.cpp"
#include "1302.deepest-leaves-sum.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	TreeNode* r = new TreeNode(50); 
	r->right = new TreeNode(54);
	r->right->left = new TreeNode(98);
	r->right->right = new TreeNode(6);
	r->right->right->right = new TreeNode(34);
	say(s.deepestLeavesSum(r));
	return 0;
}

