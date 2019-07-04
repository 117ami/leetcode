#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval
  attr_accessor :start, :end
  def initialize(s = 0, e = 0)
    @start = s
    @end = e
  end
end

# @param {Interval[]} intervals
# @return {Interval[]}
def merge(intervals)
  r = []
  intervals.sort! { |x, y| x.start <=> y.start }

  intervals.each do |i|
    if r.empty? || i.start > r[-1].end
      r << i
    else
      r[-1].end = [r[-1].end, i.end].max
    end
  end
  r
end

i = [Interval.new(2, 4), Interval.new(4, 5), Interval.new(5, 8), Interval.new(8, 9), Interval.new(10, 19)]

# i = [Interval.new(1, 4), Interval.new(4, 10)]
p merge(i)
