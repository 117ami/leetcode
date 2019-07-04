=begin
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: &ldquo;The lowest common ancestor is defined between two nodes pand qas the lowest node in T that has both pand qas descendants (where we allow a node to be a descendant of itself).&rdquo;
Given the following binary tree: root =[3,5,1,6,2,0,8,null,null,7,4]
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.
Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:
	All of the nodes' values will be unique.
	p and q are different and both values willexist in the binary tree.

=end


# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
    return root if [nil, p, q].index root
    left = lowest_common_ancestor(root.left)
    right = lowest_common_ancestor(root.right)
    !left ? right : !right ? left : root
end

arr = [nil, 0, 1]
puts "find" if arr.index(0)