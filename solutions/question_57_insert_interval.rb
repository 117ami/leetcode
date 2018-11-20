
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
class Interval
  attr_accessor :start, :end
  def initialize(s = 0, e = 0)
    @start = s
    @end = e
  end
end

# @param {Interval[]} intervals
# @param {Interval} new_interval
# @return {Interval[]}
def insert(intervals, new_interval)
  i = [*intervals.each_with_index].bsearch { |v, _| v.start > new_interval.start }
  if i.nil?
    intervals << new_interval
  else
    intervals.insert(i.last, new_interval)
  end

  r = []
  intervals.each do |i|
    if r.empty? || r[-1].end < i.start
      r << i
    else
      r[-1].end = [r[-1].end, i.end].max
    end
  end
  r
end

a = [1, 1, 3, 4]
i = []
i << Interval.new(a.shift, a.shift) until a.empty?
p i
newi = Interval.new(2, 3)
p insert(i, newi)
