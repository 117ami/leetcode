# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.
# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
#     4
# Therefore, you need to return above trees' root in the form of a list.
#  https://leetcode.com/problems/find-duplicate-subtrees/description/
require './aux.rb'

# @param {TreeNode} root
# @return {TreeNode[]}
def find_duplicate_subtrees(root)
  map = Hash.new(0)
  res = {}
  postorder = lambda do |r|
    return '#' if r.nil?
    str = r.val.to_s + ',' + postorder.call(r.left) + ',' + postorder.call(r.right)
    res[str] = r if map.key?(str)
    map[str] += 1
    return str
  end
  postorder.call(root)
  res.values
end

arr = [1, 2, 3, 4, nil, 2, 4, nil, nil, 4]
arr = [2, 2, 2, 3, nil, 3, nil]
root = construct_tree(arr)
# p root
p find_duplicate_subtrees(root)
