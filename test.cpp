
#include "aux.cpp"
#include "1382.balance-a-binary-search-tree.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi x = {1,INT_MAX,2,INT_MAX,3,INT_MAX,4,INT_MAX,INT_MAX};
	TreeNode* r = growTreeFromList(x);
	s.balanceBST(r);
	return 0;
}

