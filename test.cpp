
#include "aux.cpp"
#include "c.cpp"
#include "429.n-ary-tree-level-order-traversal.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	vector<Node*> v;
	v.pb(new Node(2, vector<Node*>{}));
	v.pb(new Node(4, vector<Node*>{}));	
	Node* r = new Node(3, v);
	vvi t = s.levelOrder(r);
	say(t);
	return 0;
}

