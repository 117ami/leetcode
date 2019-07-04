#  Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
#
# Example 1:
#
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# @param {String[]} list1
# @param {String[]} list2
# @return {String[]}
def find_restaurant(list1, list2)
  res = list1.zip(0..list1.size - 1).to_h
  r = 2 << 32
  (0..list2.size - 1).each do |i|
    next unless res.key?(list2[i])
    r = [r, i + res[list2[i]]].min
    res[list2[i]] = (res[list2[i]] + i) * -1
  end
  res.each_key.select { |k| res[k] == -r }
end

list1 = ['Shogun', 'KFC', 'Tapioca Express', 'Burger King']
list2 = ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']
list2 = ['KFC', 'Shogun', 'Burger King']
list1 = %w[afeu atzm KFC]
list2 = %w[atzm tbt KFC]
p find_restaurant(list1, list2)
