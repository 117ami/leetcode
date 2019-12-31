
#include "aux.cpp"
#include "230.kth-smallest-element-in-a-bst.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	TreeNode* root = new TreeNode(4);
	root->left = new TreeNode(2); 
	root->left->right = new TreeNode(3);
	say(s.kthSmallest(root, 2));
	return 0;
}

