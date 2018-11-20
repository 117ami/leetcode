#include "aux.cpp"
/**
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example, given a 3-ary tree:


We should return its level order traversal:


[
     [1],
     [3,2,4],
     [5,6]
]

Note:
	The depth of the tree is at most 1000.
	The total number of nodes is at most 5000.

 https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/ 
 **/
static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); 


// Definition for a Node.
class Node {
public:
    int val = NULL;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
	vector<vector<int>> levelOrder(Node* root) {
		vector<vector<int>> res; 
		helper(root, 0, res);
		return res; 
	}

	void helper(Node* root, int depth, vector<vector<int>> &res) {
		if (root == nullptr)
			return;
		if (res.begin() + depth == res.end())
			res.push_back(vector<int>(1, root->val));
		else
			res[depth].push_back(root->val);
		for (auto c : root->children)
			helper(c, depth+1, res);
    }
};

int main() { 
 Solution s; 
}
