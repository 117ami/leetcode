# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.
#
#  Example 1:
#
#   Input: "UD"
#   Output: true
#
#   Example 2:
#
#   Input: "LL"
#   Output: false
#
# rescue Exception => e
#

# @param {String} moves
# @return {Boolean}
def judge_circle(moves)
  cur = [0, 0]
  moves.each_char do |m|
    case m
    when 'U'
      cur[1] -= 1
    when 'D'
      cur[1] += 1
    when 'L'
      cur[0] -= 1
    when 'R'
      cur[0] += 1
    end
  end
  return true if cur[0].zero? && cur[1].zero?
  false
end

def judge_circle2(moves)
  moves.count('L') == moves.count('R') && moves.count('U') == moves.count('D')
end

moves = 'RLUURDDDLU'
moves = 'LLLLLUUUU'
p judge_circle(moves)
p judge_circle2(moves)
