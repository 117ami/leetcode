// https://leetcode.com/problems/delete-tree-nodes
// Medium (Difficulty)

// A tree rooted at node 0 is given as follows:
// Remove every subtree whose sum of values of nodes is zero.
// After doing so, return the number of nodes remaining in the tree.
//  
// Example 1:
// 
//  
// Constraints:
// Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
// Output: 2
// 
// xxxxxxxxxx
class Solution {
public:
    int deleteTreeNodes(int nodes, vector<int>& parent, vector<int>& value) {
        vector<int> res(nodes, 1); 
        for (int i = nodes - 1; i > 0 ; i --){
            value[parent[i]] += value[i]; 
            res[parent[i]] += value[i] == 0 ? 0 : res[i];
        }
        return res[0];
    }
};

