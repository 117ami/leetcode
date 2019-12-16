
#include "aux.cpp"
#include "662.maximum-width-of-binary-tree.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi arr = {1,3,2,5,3, INT_MAX, 9};
	TreeNode* root = growTreeFromList(arr);
	say(s.widthOfBinaryTree(root));
	return 0;
}

