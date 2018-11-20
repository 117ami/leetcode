# contain auxiliary functions for OJ
def letter?(x)
  x =~ /[[:alpha:]]/ || false
end

def digit?(x)
  x =~ /[[:digit:]]/ || false
end

def substring?(_x, _y)
  false
end

# create palindrome with n bits
def nbits_palindrome(n)
  return Array(0..9).map(&:to_s) if n == 1
  return ['00', 11, 22, 33, 44, 55, 66, 77, 88, 99].map(&:to_s) if n == 2
  res = []
  Array(0..9).each do |i|
    nbits_palindrome(n - 2).each do |m|
      res << i.to_s + m + i.to_s
    end
  end
  res
end

# p nbits_palindrome(13).size

# detemine whether string s is palindrome
def isP?(s)
  return true if s.length <= 1
  ia = 0
  ib = s.length - 1
  while ia < ib
    return false unless s[ia] == s[ib]
    ia += 1
    ib -= 1
  end
  true
end

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# Given an array, construct a tree with values from array.
def construct_tree(arr)
  root = TreeNode.new(arr.shift)
  xtd = [root]
  while !xtd.empty? && !arr.empty?
    cur_node = xtd.shift
    a, b = arr.shift(2) # doesn't matter if arr.size < 2. in this case, a, b might be nil
    cur_node.left = a.nil? ? nil : TreeNode.new(a)
    cur_node.right = b.nil? ? nil : TreeNode.new(b)
    xtd << cur_node.left unless cur_node.left.nil?
    xtd << cur_node.right unless cur_node.right.nil?
  end
  root
end

# generate a list of sz with all elements among [1..xbound]
def random_list(sz, k)
  sz.times.map { Random.rand(k) + 1 }
end

# Definition for singly-linked list.
class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

def list2arr(root)
  return [] if root.nil?
  res = []
  while root
    res << root.val
    root = root.next
  end
  res
end

def arr2list(arr)
  return nil if arr.empty?
  root = ListNode.new(arr.first)
  tmp  = root
  arr[1..-1].each { |n| tmp.next = ListNode.new(n); tmp = tmp.next; }
  root
end

# ===================================================================
# ON Graph

# parameter: parent (hash): int -> int, stores the parent node (index) of given node n
# return: n (int)
# This method finds and modifies the root parent of n, as well as its ancestors.
def find(parent, n)
  return n if n == parent[n]
  parent[n] = find(parent, parent[n])
  parent[n]
end

# Given a connect graph, this method creates the parent relations of nodes
# return: parent (hash)
# E.g., graph = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]
# parent = {0=>0, 1=>0, 2=>0}
def create_parent(graph)
  parent = (0..graph.size - 1).map { |i| [i, i] }.to_h
  graph.each_with_index do |edge, nodei|
    parent[nodei] = parent.key?(nodei) ? find(parent, nodei) : nodei
    edge.each_with_index do |iscon, nodej|
      next if iscon.zero?
      if parent[nodei] > parent[nodej]
        parent[parent[nodei]] = parent[nodei] = parent[nodej]
        find(parent, nodei)
      else
        parent[parent[nodej]] = parent[nodej] = parent[nodei]
        find(parent, nodej)
      end
    end
  end
  parent
end

# Generate an array of array with size rn X cn and initial value 1
def array_array(rn, cn, iv = 1)
  Array.new(rn) { Array.new(cn, iv) }
end

def hash_hash(iv = 0)
  Hash.new { |h, k| h[k] = Hash.new(iv) }
end
