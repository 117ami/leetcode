class MyCalendar
  def initialize
    @calenders = []
  end

  #     :type start: Integer
  #     :type end: Integer
  #     :rtype: Boolean
  def book(start, et)
    return false if @calenders.any? { |a, b| [a, start].max < [b, et].min }
    @calenders << [start, et]
    true
  end
end

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar.new()
# param_1 = obj.book(start, end)
