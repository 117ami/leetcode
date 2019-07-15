
#include "aux.cpp"
#include "1123.lowest-common-ancestor-of-deepest-leaves.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi lis = {1,2,3, 4, 5, 6, 7, 8, 9, 10};
	TreeNode * r = growTreeFromList(lis);
	TreeNode* res = s.lcaDeepestLeaves(r);
	say(res->val);
	return 0;
}

