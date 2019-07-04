
# Question 6: zigzag conversion

def convert(s, num_rows)
  return s if num_rows == 1

  cache = Array.new(num_rows) { [] }
  iter = 0
  add = true

  s.chars.each do |e|
    cache[iter] << e
    add = true if iter.zero?
    add = false if iter == num_rows - 1
    iter = add ? iter + 1 : iter - 1
  end
  cache.flatten.join('')
end

s6 = 'PAYPALISHIRING'
p convert(s6, 3)
