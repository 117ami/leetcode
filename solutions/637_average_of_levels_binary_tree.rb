# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {TreeNode} root
# @return {Float[]}
def tree2list(root, d)
  return {} if root.nil?
  [[d, root.val]].push(*tree2list(root.left, d + 1)).push(*tree2list(root.right, d + 1))
end

def average_of_levels(root)
  r = tree2list(root, 0)
  r.group_by(&:first).values.map { |v| v.map(&:last).sum / (1.0 * v.size) }
end

def average_of_levels2(root)
  todo = [root]
  r = []
  until todo.empty?
    s = 0
    c = 0
    todo.size.times do
      n = todo.shift
      next if n.nil?
      s += n.val
      c += 1
      todo << n.left
      todo << n.right
    end
    r << s / (c * 1.0) unless c.zero?
  end
  r
end

root = TreeNode.new(3)
root.left = TreeNode.new(9)
root.right = TreeNode.new(20)
root.right.left = TreeNode.new(15)
root.right.right = TreeNode.new(7)

p average_of_levels(root)
p average_of_levels2(root)
