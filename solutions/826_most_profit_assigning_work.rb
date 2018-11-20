# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.
#
# Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i].
#
# Every worker can be assigned at most one job, but one job can be completed multiple times.
#
# For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.
#
# What is the most profit we can make?
#
# Example 1:
#
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
#
# Notes:
#
#     1 <= difficulty.length = profit.length <= 10000
#     1 <= worker.length <= 10000
#     difficulty[i], profit[i], worker[i]  are in range [1, 10^5]

def max_profit_assignment(difficulty, profit, worker)
  hworker = Hash.new(0)
  worker.each { |w| hworker[w] += 1 }

  d2p = Hash.new(0)
  difficulty.each_with_index do |d, i|
    d2p[d] = [d2p[d], profit[i]].max
  end

  difficulty = d2p.keys.sort!
  profit = []
  max_profit = 0

  difficulty.each_with_index do |d, i|
    max_profit = [d2p[d], max_profit].max
    profit[i] = max_profit
  end

  r = 0
  dsize = difficulty.size
  hworker.keys.each do |k|
    i = (0..dsize - 1).bsearch { |j| difficulty[j] > k } || dsize
    next if i.zero?
    r += profit[i - 1] * hworker[k]
  end
  r
end

difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7, 4]

# difficulty = [68, 35, 52, 47, 86]
# profit = [67, 17, 1, 81, 3]
# worker = [92, 10, 85, 84, 82]
difficulty = [66, 1, 28, 73, 53, 35, 45, 60, 100, 44, 59, 94, 27, 88, 7, 18, 83, 18, 72, 63]
profit = [66, 20, 84, 81, 56, 40, 37, 82, 53, 45, 43, 96, 67, 27, 12, 54, 98, 19, 47, 77]
worker = [61, 33, 68, 38, 63, 45, 1, 10, 53, 23, 66, 70, 14, 51, 94, 18, 28, 78, 100, 16]
p max_profit_assignment(difficulty, profit, worker)
