
# @param {Integer} n
# @return {String}
def generate_next_string(s)
  c = s[0]
  arr = [[]]
  s.each_char do |e|
    arr.last.push(c) if c == e
    arr.push([e]) if c != e
    c = e
  end
  arr.map { |v| v.size.to_s + v.first }.join('')
end

def count_and_say(n)
  cid = '1'
  (2..n).map { cid = generate_next_string(cid) }
  cid 
end

# p generate_next_string('312211')
p count_and_say(7)
