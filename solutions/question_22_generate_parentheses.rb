
# Given n pairs of parentheses, write a function to generate all combinations
#   of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# @param {Integer} n
# @return {String[]}
def dp(arra, arrb)
  return [arra.join('')] if arrb.empty?
  return [arra.push(')').join('')] if arrb.size == 1 && arrb.first == ')'

  res = []
  cache = Hash[arrb.zip(0..arrb.length)]

  cache.each_key do |k|
    next if k == ')' && arra.count(')') >= arra.count('(')
    na = arra.clone.push(arrb[cache[k]])
    nb = arrb.clone
    nb.delete_at(cache[k])
    res += dp(na, nb)
    res.uniq!
  end
  res
end

def loop_out(left, right, s)
  r = []
  r << s if left == 0 && right == 0
  r += loop(left - 1, right, s + '(') if left > 0
  r += loop(left, right - 1, s + ')') if left < right
  r
end

def generate_parenthesis(n)
  r = []
  loop = lambda do |left, right, s = ''|
    if left == 0 && right == 0
      r << s
      return
    end
    loop.call(left - 1, right, s + '(') if left > 0
    loop.call(left, right - 1, s + ')') if left < right
  end
  loop.call(n, n)
  r
end

p generate_parenthesis(4)
