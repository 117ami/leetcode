# @param {Integer} x
# @param {Integer} y
# @param {Integer} bound
# @return {Integer[]}
def powerful_integers(x, y, bound)
  res = {}
  ibound = x == 1 ? 1 : Math.log(bound, x)
  jbound = y == 1 ? 1 : Math.log(bound, y)
  0.upto(ibound).each do |i|
    0.upto(jbound).each do |j|
      pn = x**i + y**j
      break if pn > bound

      res[pn] = nil
    end
  end

  res.keys
end

bound = 100
x = 1
y = 2

p powerful_integers(x, y, bound)
