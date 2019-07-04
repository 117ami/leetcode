/*
 * @lc app=leetcode id=589 lang=cpp
 *
 * [589] N-ary Tree Preorder Traversal
 *
 * https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
 *
 * algorithms
 * Easy (66.88%)
 * Total Accepted:    37.6K
 * Total Submissions: 56.2K
 * Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
 *
 * Given an n-ary tree, return the preorder traversal of its nodes' values.
 * 
 * For example, given a 3-ary tree:
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Return its preorder traversal as: [1,3,5,6,2,4].
 * 
 * 
 * 
 * Note:
 * 
 * Recursive solution is trivial, could you do it iteratively?
 * 
 */
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> ans = {}; 
        if (root == NULL) return ans; 
        stack<Node *> s; 
        s.push(root); 

        while (s.size() > 0) {
            Node *e = s.top(); 
            ans.push_back(e->val); 
            s.pop();
            if (e->children.size() > 0) {
                for(auto it = e->children.rbegin(); it != e->children.rend(); it ++) {
                    s.push(*it); 
                }
            }
        }
        return ans; 
    }
};

static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();

// int main(int argc, char const *argv[]) {
// 	Solution s;
// 	return 0;
// }

