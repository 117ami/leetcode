def prefixes_div_by5(a)
  ans = []
  x = 0
  t = [1, 2, 4, 3, 1]
  a.each_with_index do |n, _i|
    x = x * 2 + n
    x = x % 5
    ans << x.zero?
  end
  ans
end

a = [0, 1, 1, 1, 1, 1]
a = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0]
p prefixes_div_by5(a)


# @param {Integer} n
# @return {String}
def base_neg2(n)
  y = 0
  x = tn = n
  sn = ''
  loop do
    sn = x.to_s(2).reverse
    y = 0
    sn.each_char.with_index do |c, i|
      y += 2**i if i.odd? && c == '1'
    end
    return sn.reverse if x - 2 * y == n
    x += n - (x - 2 * y)
  end
  sn
end

n = 4
p base_neg2(n)

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# @param {ListNode} head
# @return {Integer[]}
def list2arr(root)
  return [] if root.nil?

  res = []
  while root
    res << root.val
    root = root.next
  end
  res
end

def next_larger_nodes(_head)
  # arr = list2arr(head)
  arr = [1, 7, 5, 1, 9, 2, 5, 1]
  # arr = [2,7,4,3,5]
  stack = []
  ans = []
  arr.each_with_index do |n, i|
    while !stack.empty? && stack[-1].first < n
      ans << [n, stack[-1].last]
      stack.pop
     end
    stack << [n, i]
  end
  stack = stack.map { |v| [0, v.last] }
  (ans + stack).sort_by(&:last).map(&:first)
end

head = 0
# p next_larger_nodes(head)

# @param {Integer[][]} a
# @return {Integer}
def num_enclaves(a)
  trans = lambda do |i, j|
    return if i < 0 || j < 0 || i >= a.size || j >= a[0].size || a[i][j].zero?

    a[i][j] = 0
    [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]].each do |ni, nj|
      trans.call(ni, nj)
    end
  end
  0.upto(a.size - 1).each do |i|
    trans.call(i, 0)
    trans.call(i, a[0].size - 1)
  end

  0.upto(a[0].size - 1).each do |j|
    trans.call(0, j)
    trans.call(a.size - 1, j)
  end

  ans = 0
  0.upto(a.size - 1).each do |i|
    0.upto(a[0].size - 1).each do |j|
      ans += 1 if a[i][j] == 1
    end
  end
  ans
end

a = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
a = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]

# p num_enclaves(a)
