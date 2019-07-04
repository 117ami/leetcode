class MyCircularQueue

=begin
    Initialize your data structure here. Set the size of the queue to be k.
    :type k: Integer
=end
    def initialize(k)
		@arr = []
		@sz = k         
    end


=begin
    Insert an element into the circular queue. Return true if the operation is successful.
    :type value: Integer
    :rtype: Boolean
=end
    def en_queue(value)
        return false if @arr.size == @sz
        @arr << value
        true
    end


=begin
    Delete an element from the circular queue. Return true if the operation is successful.
    :rtype: Boolean
=end
    def de_queue()
        return false if @arr.empty?
        # shift not pop, queue isn't stack .
        @arr.shift
        true
    end


=begin
    Get the front item from the queue.
    :rtype: Integer
=end
    def front()
        return -1 if @arr.empty?
        @arr[0]
    end


=begin
    Get the last item from the queue.
    :rtype: Integer
=end
    def rear()
        return -1 if @arr.empty?
        @arr.last
    end


=begin
    Checks whether the circular queue is empty or not.
    :rtype: Boolean
=end
    def is_empty()
		@arr.empty?        
    end


=begin
    Checks whether the circular queue is full or not.
    :rtype: Boolean
=end
    def is_full()
        @arr.size == @sz
    end


end

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue.new(k)
# param_1 = obj.en_queue(value)
# param_2 = obj.de_queue()
# param_3 = obj.front()
# param_4 = obj.rear()
# param_5 = obj.is_empty()
# param_6 = obj.is_full()