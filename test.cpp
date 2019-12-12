
#include "aux.cpp"
#include "1028.recover-a-tree-from-preorder-traversal.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	string t = "1-401--349---90--88"; 
	t = "1-2--3---4-5--6---7";
	TreeNode* root = s.recoverFromPreorder(t);
	vvi vs = valuesOfTree(root); 
	say(vs);
	return 0;
}

