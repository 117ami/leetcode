# coding: utf-8

# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k)
  factorial = lambda do |n|
    (2..n).inject(:*) || 1
  end

  kperm = lambda do |a, m|
    f = factorial.call(a.size)
    r = []
    until a.empty?
      f /= a.size
      r << a.delete_at(m / f)
      m = m % f
    end
    r.join
  end
  kperm.call(Array(1..n), k - 1)
end

def get_permutation_2(n, k)
  Array(1..n).permutation(n).to_a[k - 1].join
end

n = 4
k = 2
p get_permutation(n, k)
p get_permutation_2(n, k)
