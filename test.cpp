
#include "aux.cpp"
#include "655.print-binary-tree.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vi vs = {1, 2};
	vs = {1, 2, 3, INT_MIN, 4};
	TreeNode* root = growTreeFromList(vs);
	vvs res = s.printTree(root); 
	say(res[0].size());
	say(res);

	float i = 9.1, pi = pow(9, 2); 
	cout << typeid(pi).name() << endl; 
	return 0;
}

