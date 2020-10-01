// Containers
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <numeric>


#include "conf.d/say.h"

using namespace std; 
int dirs[5] = {-1, 0, 1, 0, -1};

// --------------------------------------------------------
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Codec {
public:
    // Encodes an n-ary tree to a binary tree.
    TreeNode* encode(Node* root) {
        TreeNode* bt; 
        if(root == nullptr) return bt; 
        bt = new TreeNode(root->val);
        if (root->children.size() > 0) bt->left = encode(root->children[0]);

        TreeNode* r = bt->left;
        for(int i=1; i<root->children.size(); i++) {
            r->right = encode(root->children[i]);
            r = r->right;
        }
        return bt; 
    }
	
    // Decodes your binary tree to an n-ary tree.
    Node* decode(TreeNode* root) {
        Node* nt; 
        if(root==nullptr) return nt; 
        nt = new Node(root->val);
        vector<Node*> ch; 
        TreeNode* r = root->left;
        while(r) {
            ch.push_back(decode(r));
            r = r->right;
        }
        nt->children = ch; 
        return nt;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(root));


int main() {
  Solution s;
  
}