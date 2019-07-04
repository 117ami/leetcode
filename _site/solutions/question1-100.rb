#!/usr/bin/ruby -w
require 'prime'

def say(*arg)
  print '=>>', arg, "\n"
end

# p question2(s)
# length_of_longest_substring(s)

def q3(x)
  return 0 if x == 0
  flag = 1
  flag = -1 if x < 0
  x = x.abs
  a = x.to_s.split('').reverse!.drop_while { |i| i.to_i < 1 }
  res = a.join('').to_i
  return 0 if res > 2**31 - 1
  flag * res
end

p q3(-123_232_323_394_859_437)
p q3(1_563_847_412)
p 2**31 - 1

# ---------------------------------------------------------------------------------------------------
def q4(nums1, nums2) # question 4. Median of Two Sorted Arrays
  m = nums1.length
  n = nums2.length
  nums1.push(nums2).flatten!.sort!
  sz = m + n

  if (m + n).even?
    return (nums1[(sz - 2) / 2] + nums1[sz / 2]) / 2.0
  else
    return nums1[(sz - 1) / 2]
  end
end

na = [3, 3, 4, 11, 13, 14, 18, 27, 32, 38, 41, 41, 48, 50, 51, 54, 56, 60, 60, 65, 67, 73, 78, 78, 78, 84, 91, 91, 94, 97]
nb = [2, 7, 9, 12, 18, 18, 26, 27, 31, 31, 31, 31, 32, 46, 47, 47, 53, 54, 55, 56, 61, 62, 68, 71, 81, 82, 83, 83, 85]

say q4(na, nb)

# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
def q9(x)
  return true if x == 0
  return false if (x < 0) || (x % 10 == 0)
  m = 0
  while x > m
    m = x % 10 + m * 10
    x /= 10
    p x, m
  end
  return true if (x == m) || (m / 10 == x)
  false
end

p q9(12_321)

# ---------------------------------------------------------------------------------------------------
def dp(s, p, i, j, memo)
  unless memo.key?([i, j]) # not explored before
    if j == p.length
      ans = i == s.length
    else
      first_match = i < s.length && [s[i], '.'].include?(p[j])
      ans = if j + 1 < p.length && p[j + 1] == '*'
              dp(s, p, i, j + 2, memo) || first_match && dp(s, p, i + 1, j, memo)
            else
              first_match && dp(s, p, i + 1, j + 1, memo)
            end
    end
    memo[[i, j]] = ans
  end
  memo[[i, j]]
end

def is_match(s, p) # question 10 regular expression match
  dp(s, p, 0, 0, {})
end

s10 = 'aaaaabaccbbccababa'
p10 = 'a*b*.*c*c*.*.*.*c'
say is_match(s10, p10)

# ---------------------------------------------------------------------------------------------------
def q11(height) # question 11 container with most water
  sz = height.length
  maxarea = 0
  l = 0
  r = sz - 1

  while l < r
    maxarea = [maxarea, [height[l], height[r]].min * (r - l)].max
    if height[l] < height[r]
      l += 1
    # hl = height[l]
    # while height[l] <= hl and l < r
    #   l += 1
    # end
    else
      r -= 1
      # hr = height[r]
      # while height[r] <= hr and l < r
      #   r -= 1
      # end
    end
  end

  maxarea
end

# ---------------------------------------------------------------------------------------------------
def int_to_roman(num) # question 12
  m = ['', 'M', 'MM', 'MMM']
  c = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
  x = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
  i = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
  m[num / 1000] + c[(num % 1000) / 100] + x[(num % 100) / 10] + i[(num % 10)]
end

# ---------------------------------------------------------------------------------------------------
def q13(s) # roman to integer
  roman = 'IVXLCDM'.split('')
  value = [1, 5, 10, 50, 100, 500, 1000]
  h = Hash[roman.zip(value)]
  a = s.split('')
  res = 0

  (0..a.size - 2).each do |i|
    if h[a[i]] < h[a[i + 1]]
      res -= h[a[i]]
    else
      res += h[a[i]]
    end
  end
  res += h[a.last]
  res
end

p q13('MCMLXXIII')

# ---------------------------------------------------------------------------------------------------

def q14(strs)                   #  Longest Common Prefix
  sz = strs.size
  return '' if sz == 0
  return strs[0] if sz == 1

  res = strs.shift.split('')
  strs.each do |e|
    a = e.split('')
    return '' if a.first != res.first

    tmpsz = [a.size, res.size].min - 1
    res = res.take(tmpsz + 1)

    (0..tmpsz).each do |i|
      print i, res[i], a[i], " ==\n"
      if res[i] != a[i]
        res = res.take(i)
        break
      end
    end
  end

  res.join
end

strs = ['abandon', 'abause', 'aba problem']
strs = %w[aa a]
p q14(strs)

def q15(nums)                   # 3sum
  nums.sort!
  maxid = nums.size - 1
  return [] if (maxid < 2) || (nums.first > 0) || (nums.last < 0)
  return [[0, 0, 0]] if (nums.first == 0) && (nums.last == 0) # all elements in nums are 0
  res = {}

  for i in (0..maxid - 2) do
    break if nums[i] > 0 # no need for further exploration
    rest = 0 - nums[i]
    front = i + 1
    back = maxid

    while front < back
      ln = nums[front]
      hn = nums[back]
      break if hn < 0 # in such case, no suitable triplet can be found

      if ln + hn == rest
        triplet = [nums[i], ln, hn]
        res.store(triplet, nil) unless res.key?(triplet)
        front += 1
        back -= 1
      elsif ln + hn < rest
        front += 1
      else
        back -= 1
      end
    end
  end

  res.keys
end

def q15_2(nums)
  result = []
  cache = {}

  nums.each do |e|
    if cache.key?(e)
      cache[e] += 1
    else
      cache[e] = 1
    end
  end

  negatives = cache.keys.select { |e| e < 0 }
  positives = cache.keys.select { |e| e > 0 }

  negatives.each do |n|
    positives.each do |m|
      r = 0 - n - m
      next if (r < n) || (r > m) || !cache.key?(r)
      next if ((r == n) || (r == m)) && (cache[r] < 2)
      result << [n, m, r]
    end
  end

  result << [0, 0, 0] if cache.key?(0) && (cache[0] >= 3)
  result
end

# nums = [3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]

nums2 = [0, 0, 0]

p q15_2(nums2)

# ---------------------------------------------------------------------------------------------------
def q20(s) # question 20. Valid Parantheses
  return true if s == ''
  arr = s.chars
  cache = [arr[0]]
  arr.shift

  until arr.empty?
    c = arr.shift
    case c
    when ')'
      return false if cache[-1] != '('
      cache.pop
    when  ']'
      return false if cache[-1] != '['
      cache.pop
    when  '}'
      return false if cache[-1] != '{'
      cache.pop
    else
      cache.push(c)
    end
  end

  return false unless cache.empty?
  true
end

s20 = '()[]{}'
say 'QUESTION 20', q20(s20)

# ---------------------------------------------------------------------------------------------------
# A key point is that: "It doesn't matter what you leave beyond the new length."
# so we can just replace the some duplicate elements
def q26(nums) #  question 26. Remove Duplicates from Sorted Array.
  return 0 if nums.empty?

  i = 0
  (1..nums.length - 1).each do |j|
    if nums[j] != nums[i]
      i += 1
      nums[i] = nums[j]
    end
  end
  i + 1
end

nums = [2, 2, 2, 2, 3, 4, 5, 6]
# nums = [1, 1]
say q26(nums)
