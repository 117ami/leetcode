# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.
#
# @param {String[]} time_points
# @return {Integer}
def find_min_difference(time_points)
  ntimes = {}
  time_points.each do |stime|
    h, m = stime.split(':').map(&:to_i)
    p stime if ntimes.key?(h * 60 + m)
    return 0 if ntimes.key?(h * 60 + m)
    ntimes[h * 60 + m] = nil
  end
  ntimes = ntimes.keys.sort
  res = (1..ntimes.size - 1).map { |i| ntimes[i] - ntimes[i - 1] }.min
  [res, ntimes[0] + 1440 - ntimes[-1]].min
end

time_points = ['23:59', '04:54', '03:43', '23:59']
time_points = ['00:00', '23:59', '00:00']
time_points = ['05:31', '22:08', '00:35']
p find_min_difference(time_points)

time_points = 100.times.map { [Random.rand(24), Random.rand(60)].join(':') }
p find_min_difference(time_points)
