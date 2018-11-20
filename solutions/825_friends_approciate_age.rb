# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.
#
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
#
#     age[B] <= 0.5 * age[A] + 7
#     age[B] > age[A]
#     age[B] > 100 && age[A] < 100
#
# Otherwise, A will friend request B.
#
# Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
#
# How many total friend requests are made?

# @param {Integer[]} ages
# @return {Integer}
def num_friend_requests(ages)
  cache = Hash.new(0)
  ages.each { |a| cache[a] += 1 }
  r = cache.each_pair.map { |k, v| k > 14 ? v * (v - 1) : 0 }.reduce(:+)
  ages = cache.keys.sort.reverse

  (0..ages.size - 2).each do |i|
    j = (i..ages.size - 1).bsearch { |j| (ages[j] - 7) * 2 <= ages[i] }
    j = ages.size if j.nil?
    j -= 1
    next if j == i
    (i + 1..j).each { |k| r += cache[ages[k]] * cache[ages[i]] }
    # p [i, ages[i], j, " = ", j - i, r]
  end
  r
end

ages = [20, 100, 30, 110, 120, 120, 110]
# ages = [16, 17, 18]
ages = [16, 16, 16, 16, 17, 17]
ages = [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]
ages = [16, 16]
p num_friend_requests(ages)
