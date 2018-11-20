# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

# @param {Integer[][]} m
# @return {Integer[][]}
def gen_coor(i, j)
  [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j], [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
end

def legal_coor?(coor, n, m)
  coor[0] >= 0 && coor[0] <= n && coor[1] >= 0 && coor[1] <= m
end

def image_smoother(m)
  res = Array.new(m.size) { Array.new(m[0].size, 0) }
  (0..m.size - 1).each do |i|
    (0..m[0].size - 1).each do |j|
      counter = xsum = 0
      gen_coor(i, j).each do |coor|
        next unless legal_coor?(coor, m.size - 1, m[0].size - 1)
        counter += 1
        xsum += m[coor[0]][coor[1]]
      end
      res[i][j] = xsum / counter
    end
  end
  res
end

p gen_coor(2, 3)

m = [[1,1,1],
 [1,0,1],
 [1,1,1]]
p image_smoother(m)
