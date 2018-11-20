# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

# @param {Integer[][]} points
# @return {Float}
def area(p1, p2, p3)
  a = Math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
  b = Math.sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
  c = Math.sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)
  s = (a + b + c) / 2.0
  r = s * (s - a) * (s - b) * (s - c)
  return 0 if r <= 0
  Math.sqrt(r)
end

def largest_triangle_area(points)
  ma = 0
  sz = points.size
  (0..sz - 1).each do |i|
    (i + 1..sz - 1).each do |j|
      (j + 1..sz - 1).each do |k|
        ma = [ma, area(points[i], points[j], points[k])].max
      end
    end
  end
  ma
end

points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
points = [[35, -23], [-12, -48], [-34, -40], [21, -25], [-35, -44], [24, 1], [16, -9], [41, 4], [-36, -49], [42, -49], [-37, -20], [-35, 11], [-2, -36], [18, 21], [18, 8], [-24, 14], [-23, -11], [-8, 44], [-19, -3], [0, -10], [-21, -4], [23, 18], [20, 11], [-42, 24], [6, -19]]
p largest_triangle_area(points)
