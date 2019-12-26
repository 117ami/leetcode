
#include "aux.cpp"
#include "889.construct-binary-tree-from-preorder-and-postorder-traversal.cpp"

int main(int argc, char const *argv[]) {
	// Solution s;
	vi a = {0, 1,2,3,4,5};
	vi part(a.begin()+ 1, a.end()-1);
	say(part);
	return 0;
}

