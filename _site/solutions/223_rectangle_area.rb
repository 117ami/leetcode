# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# Example:
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# Note:
# Assume that the total area is never beyond the maximum possible value of int.
#

# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @param {Integer} d
# @param {Integer} e
# @param {Integer} f
# @param {Integer} g
# @param {Integer} h
# @return {Integer}
def compute_area(a, b, c, d, e, f, g, h)
	total_area = area(a, b, c, d) + area(e, f, g, h)
	return total_area if e >= c || a >= g || f >= d || b >= h
	total_area - area([a, e].max, [b, f].max, [c, g].min, [d, h].min)
end

def area(a, b, c, d)
	(c - a) * (d - b)
end

p compute_area(-3, 0, 3, 4, 0, -1, 9, 2)