# @param {Integer[][]} points
# @return {Boolean}
def is_boomerang(points)
  points.sort_by!(&:first)
  points.uniq!
  return false if points.size != 3

  a, b, c = points
  return true if b.first - a.first == 0 && c.first - a.first != 0
  return false if a.first == b.first && a.first == c.first

  return false if (b.last - a.last) * (c.first - a.first) == (c.last - a.last) * (b.first - a.first)

  true
end

# @param {TreeNode} root
# @return {TreeNode}
def bst_to_gst(root)
  return root if root.nil?

  helper = lambda do |r, v|
    return v if r.nil?

    if r.left.nil? && r.right.nil?
      r.val += v
      return r.val
    end

    r.val += helper.call(r.right, v) if r.right
    return r.left.nil? ? r.val : helper.call(r.left, r.val)
  end
  helper.call(root, 0)
  root
end

require './aux.rb'
# root = construct_tree([4, 1, 6, 0, 2, 5, 7, nil, nil, nil, 3, nil, nil, nil, 8])
# p bst_to_gst(root)

def min_score_triangulation(a)
    return a.reduce(:*) if a.size == 3
    if a.size == 4
    	product = a.reduce(:*)
    	return [product / a.first + product/a[2], product / a[1] + product / a.last]
    end
    dp = Array.new(a.size){Array.new(a.size, 0)}

    3.upto(a.size).each do |len|
    	0.upto(a.size - len).each do |i|
    		j = i + len
    		dp[i][j] = 
    	end
    end
end

a = [3, 7, 4, 5]
p min_score_triangulation(a)
