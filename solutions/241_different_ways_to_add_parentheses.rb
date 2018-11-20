# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

# @param {String} input
# @return {Integer[]}
def calculate(a)
  return a[0].to_i + a[-1].to_i if a[1] == '+'
  return a[0].to_i - a[-1].to_i if a[1] == '-'
  a[0].to_i * a[-1].to_i
end

def diff_ways_to_compute(input)
  poss = []
  comp = lambda do |quo|
    if quo.size == 3
      poss << calculate(quo)
    elsif quo.count('-') + quo.count('+') == 0
      r = quo.select { |i| i =~ /\d+/ }.map(&:to_i).reduce(:*)
      # p quo.select{|i| i.to_s=~/\d+/}.map(&:to_i)
      # r = 1
      # quo.each_with_index {|c, i| r *= c.to_i if i.odd?;}
      # p [quo, r]
      # res[r] = nil
      poss << r
    else
      (1..quo.size - 1).step(2).each do |i|
        xquo = quo.dup
        xquo[i - 1..i + 1] = calculate(quo[i - 1..i + 1]).to_s
        comp.call(xquo)
      end
    end
  end
  comp.call(input.split(/([?\+\-\*])/))
  poss.sort
end

input = '2*3-4*5'
input = '2-1-1'
p diff_ways_to_compute(input)
