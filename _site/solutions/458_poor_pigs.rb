#
# There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
# Answer this question, and write an algorithm for the follow-up general case.
# Follow-up:
# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
#
# @param {Integer} buckets
# @param {Integer} minutes_to_die
# @param {Integer} minutes_to_test
# @return {Integer}
def poor_pigs(buckets, minutes_to_die, minutes_to_test)
  pigs = 0
  pigs += 1 while (minutes_to_test / minutes_to_die + 1)**pigs < buckets
  pigs
end

p poor_pigs(1000, 15, 60)
