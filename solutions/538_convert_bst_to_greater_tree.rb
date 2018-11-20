# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {TreeNode}
def convert_bst(root)
  nsum = 0
  convert = lambda do |cur|
    return if cur.nil?
    convert.call(cur.right)
    cur.val += nsum
    nsum = cur.val
    convert.call(cur.left)
  end
  convert.call(root)
  root
end
