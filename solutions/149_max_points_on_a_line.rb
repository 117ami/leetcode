# # Definition for a point.
# class Point
#   attr_accessor :x, :y
#   def initialize(x = 0, y = 0)
#     @x = x
#     @y = y
#   end
# end

# @param {Point[]} points
# @return {Integer}
def max_points(points)
  points = points.map { |pt| [pt.x + 1, pt.y + 1] }
  return points.size if points.size < 2

  occurrences = points.group_by(&:itself).values.map { |v| [v.first.join('.'), v.size] }.to_h

  points.sort_by!(&:last).sort_by!(&:first)
  res = [1, points.group_by(&:first).values.map(&:size).max].max
  res = [res, points.group_by(&:last).values.map(&:size).max].max

  lines = Hash.new { |h, k| h[k] = {} }

  points.each_with_index do |_pr, idx|
    pa = points[idx]
    (idx + 1).upto(points.size - 1).each do |jdx|
      pb = points[jdx]
      next if pa.first == pb.first || pa.last == pb.last

      ratio = (pb.last - pa.last) * 1.0 / (pb.first - pa.first)
      base_point = pb.first - (pa.first - pb.first) * pb.last * 1.0 / (pa.last - pb.last)
      l_key = [ratio, base_point].join('#')
      lines[l_key][pa.join('.')] = occurrences[pa.join('.')]
      lines[l_key][pb.join('.')] = occurrences[pb.join('.')]
      # p [pa, pb, ratio, base_point]
    end
  end
  
  return res if lines.empty?
  [res, lines.values.map { |h| h.values.reduce(:+) }.max].max
end

# purpoints = [[0, 0], [0, 0]]
# # purpoints = [[0, 0], [94_911_151, 94_911_150], [94_911_152, 94_911_151]]
# purpoints = [[0,0],[1,1],[0,0]]
# purpoints = [[0, 0], [1, 0]]
# purpoints = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# points = purpoints.map { |pt| Point.new(pt.first, pt.last) }
# p max_points(points)
