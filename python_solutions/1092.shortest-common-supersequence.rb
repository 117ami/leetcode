#!/usr/bin/ruby

# contain auxiliary functions for OJ
def is_letter?(x)
  x =~ /[[:alpha:]]/ || false
end

def is_digit?(x)
  x =~ /[[:digit:]]/ || false
end

# determinate is s.chars is a sublist of t.chars. e.g., is_sub?('abc', 'apbpcp') == True
def is_sub?(s, t)
  i = j = 0
  while i < s.size && j < t.size
    i += 1 if s[i] == t[j]
    j += 1
  end
  i == s.size
end

# ======================== numbers =========================
# Given a number N, return a string consisting of [0..k-1] that represents \
# its value in base k, which might be negative.
def toBase(n, base)
  return n.to_s(base) if base > 0
  return '0' if n.zero?

  digits = []
  while n != 0
    n, remainder = n.divmod(base)
    if remainder < 0
      n += 1
      remainder -= base
    end
    digits << remainder
  end
  digits.join.reverse
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

def list2arr(head)
  res = []
  while head
    res << head.val
    head = head.next
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

# A native Priority Queue
class PriorityQueue
  def elements
    @es
  end

  def initialize
    @es = []
  end

  def empty?
    @es.empty?
  end

  def size
    @es.size
  end

  def <<(x)
    push(x)
  end

  def shift
    @es.shift
  end

  def pop
    @es.pop
  end

  def push(x) # x is assumed to be an integer or a string
    return pusharray(x) if x.is_a?(Array)

    idx = (0..@es.size - 1).bsearch { |i| @es[i] < x } || @es.size
    @es.insert(idx, x)
  end

  def pusharray(x) # x is assumed to be an array
    idx = (0..@es.size - 1).bsearch { |i| @es[i].first <= x.first } || @es.size
    @es.insert(idx, x)
  end
end

# decide whether a non-empty array, containing only positive integers, can be partitioned
# into two equal subsets
def can_partition(nums)
  mus = nums.reduce(:+)
  return false if mus.odd?

  target = mus / 2
  seen = {}

  dfs = lambda do |i, acc|
    return true if acc == target
    return false if i >= nums.size || acc > target

    key = "#{acc},#{i}"
    return seen[key] if seen.key?(key)

    res = dfs.call(i + 1, acc + nums[i]) || dfs.call(i + 1, acc)
    seen[key] = res
    res
  end
  dfs.call(0, 0)
end

def gcd(a, b)
  b == 0 ? a : gcd(b, a.modulo(b))
end

# t is either a string or an array
def counter(t)
  cter = Hash.new(0)
  arr = t.is_a?(String) ? t.chars : t
  arr.each do |c|
    cter[c] += 1
  end
  cter
end

require 'prime'
def prime_factors(n)
  Prime.prime_division(n).map(&:first)
end

def parallel(*values)
  values
end

# shortest super-sequence
def scs(s, t)
  # return shortest common super-sequence
  m, n = parallel(s.size, t.size)
  dp = array_array(m + 1, n + 1, 0)

  0.upto(m).each do |i|
    0.upto(n).each do |j|
      dp[i][j] = if i == 0 || j == 0
                   0
                 elsif s[i - 1] == t[j - 1]
                   dp[i - 1][j - 1] + 1
                 else
                   [dp[i - 1][j], dp[i][j - 1]].max
                end
    end
  end
  i, j, idx, res = parallel(m, n, m + n - dp.last.last, ['*'] * (m + n - dp.last.last))

  while i > 0 && j > 0
    if s[i - 1] == t[j - 1]
      res[idx - 1], i, j = parallel(s[i - 1], i - 1, j - 1)
    elsif dp[i - 1][j] > dp[i][j - 1]
      res[idx - 1], i = parallel(s[i - 1], i - 1)
    else
      res[idx - 1], j = parallel(t[j - 1], j - 1)
    end
    idx -= 1
 end

  i, s = parallel(j, t) if j > 0
  res[idx - 1], idx, i = parallel(s[i - 1], idx - 1, i - 1) while i > 0
  res.join
end

#
# @lc app=leetcode id=1092 lang=ruby
#
# [1092] Shortest Common Supersequence
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (43.85%)
# Total Accepted:    1.4K
# Total Submissions: 3.2K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
#
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
#
#
#
# Example 1:
#
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a substring of "cabac" because we can delete the first "c".
# str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
#
#
#
#
# Note:
#
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
#
#
# @param {String} str1
# @param {String} str2
# @return {String}
def shortest_common_supersequence(s, t)
  scs(s, t)
end

# p shortest_common_supersequence('abac', 'cab')
