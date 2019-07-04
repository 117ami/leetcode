# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# @param {Integer[][]} a
# @return {Integer[][]}
def flip_and_invert_image(a)
  a.map { |b| b.reverse.map { |c| 1 - c } }
end

a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
a = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
p flip_and_invert_image(a)
