#
# @lc app=leetcode id=855 lang=ruby
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (35.42%)
# Total Accepted:    9.4K
# Total Submissions: 26.5K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
#
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
#
#
#
# Example 1:
#
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
#
#
# ​​​​​​​
#
# Note:
#
#
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
#
#
#
class ExamRoom
  #     :type n: Integer
  def initialize(n)
    @taken = {}
    @n = n
  end

  #     :rtype: Integer
  def seat
    if @taken.empty?
      @taken[0] = nil
      0
    else
      tkeys = @taken.keys.sort
      res = maxdist = -1
      tkeys.each_with_index do |n, i|
        break if i == tkeys.size - 1
        next if maxdist >= (tkeys[i + 1] - n) / 2

        maxdist = (tkeys[i + 1] - n) / 2
        res = maxdist + n
      end
      # p [res, maxdist]
      if tkeys.first >= maxdist
          res = 0
          maxdist = tkeys.first
      end 
      res = @n - 1 if @n - 1 - tkeys.last > maxdist
      @taken[res] = nil
      res
    end
  end

  #     :type p: Integer
  #     :rtype: Void
  def leave(p)
    @taken.delete(p)
  end
end

# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom.new(10)
p obj.seat
p obj.seat
p obj.seat
# p obj.seat
obj.leave(0)
obj.leave(4)
p obj.seat
