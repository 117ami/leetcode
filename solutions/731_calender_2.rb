class MyCalendarTwo
  def initialize
    @overlaps = []
    @calenders = []
  end

  #     :type start: Integer
  #     :type end: Integer
  #     :rtype: Boolean
  def book(st, et)
    return false if @overlaps.any? { |si, ei| st < ei && si < et }
    @calenders.each do |a, b|
      next if st >= b || et <= a
      @overlaps << [[st, a].max, [et, b].min]
    end
    @calenders << [st, et]
    true
  end
end

# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo.new
p obj.book(10, 20)
p obj.book(10, 40)
p obj.book(5, 11)
