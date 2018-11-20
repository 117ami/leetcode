
arr = [10, 5, -3, 3, 2, nil, 11, 3, -2, nil, 1]

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

def array2tree(arr)
  queue = [TreeNode.new(arr.shift)]
  head = queue.first

  until arr.empty?
    if arr[0].nil?
      queue[0].left = nil
      arr.shift
    else
      queue[0].left = TreeNode.new(arr.shift)
      queue << queue[0].left
    end

    if arr[0].nil?
      queue[0].right = nil
      arr.shift
    else
      queue[0].right = TreeNode.new(arr.shift)
      queue << queue[0].right
    end

    queue.shift
  end
  head
end
