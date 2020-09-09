
#include "aux.cpp"
#include "1022.sum-of-root-to-leaf-binary-numbers.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	TreeNode * r = new TreeNode(1);
	r->left = new TreeNode(0);
	r->left->left = new TreeNode(0);
	r->left->right = new TreeNode(1);
	r->right = new TreeNode(1);
	r->right->left = new TreeNode(0);
	r->right->right = new TreeNode(1);
	say(s.sumRootToLeaf(r));

	return 0;
}

