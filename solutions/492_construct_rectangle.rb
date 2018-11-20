
#  For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
#
# 1. The area of the rectangular web page you designed must equal to the given target area.
#
# 2. The width W should not be larger than the length L, which means L >= W.
#
# 3. The difference between length L and width W should be as small as possible.
#
# You need to output the length L and the width W of the web page you designed in sequence.
# @param {Integer} area
# @return {Integer[]}
def construct_rectangle(area)
  width = 1
  r = [area, 1]
  loop do
    len = area / width
    b = area % width
    return r if len < width
    r = [len, width] if b.zero?
    width += 1
  end
end

area = Random.rand(1..10_000)
p area
p construct_rectangle(6)
