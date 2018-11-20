=begin
Write a class RecentCounter to count recent requests.
It has only one method:ping(int t), where t represents some time in milliseconds.
Return the number of pings that have been made from 3000 milliseconds ago until now.
Any ping with time in [t - 3000, t] will count, including the current ping.
It is guaranteed that every call to ping uses a strictly larger value oft than before.

Example 1:
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]

Note:
	Each test case will have at most 10000 calls to ping.
	Each test case will callping with strictly increasing values of t.
	Each call to ping will have 1 <= t <= 10^9.


 https://leetcode.com/problems/number-of-recent-calls/description/ 
=end
require './aux.rb'

class RecentCounter
    def initialize()
        @vs = []
    end


=begin
    :type t: Integer
    :rtype: Integer
=end
    def ping(t)
    	@vs << t 
        @vs.shift until t - @vs.first <= 3000
        @vs.size
    end


end

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter.new()
p obj.ping(1)
p obj.ping(100)
p obj.ping(3001)
p obj.ping(3002)
