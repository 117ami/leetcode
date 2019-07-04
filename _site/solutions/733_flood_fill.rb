#
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.
# At the end, return the modified image.
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
#
#  https://leetcode.com/problems/flood-fill/description/
require './aux.rb'

# @param {Integer[][]} image
# @param {Integer} sr
# @param {Integer} sc
# @param {Integer} new_color
# @return {Integer[][]}
def flood_fill(image, sr, sc, new_color)
  seen = {}
  source_color = image[sr][sc]
  helper = lambda do |idx, jdx|
    return if seen.key?([idx, jdx].join('.'))
    image[idx][jdx] = new_color
    [[idx - 1, jdx], [idx + 1, jdx], [idx, jdx - 1], [idx, jdx + 1]].each do |i, j|
      next if i < 0 || j < 0 || i >= image.size || j >= image[0].size || image[i][j] != source_color
      image[i][j] = new_color
      seen[[idx, jdx].join('.')] = nil
      helper.call(i, j)
    end
  end
  helper.call(sr, sc)
  image
end

image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1]
]

image = [[0, 0, 0], [0, 1, 0]]

p flood_fill(image, 1, 1, 2)
