class LFUCache
  #     :type capacity: Integer
  def initialize(capacity)
    @cache = {}
    @frequency = Hash.new(0)
    @capacity = capacity
    @rentused = {}
  end

  #     :type key: Integer
  #     :rtype: Integer
  def get(key)
    if @cache.key?(key)
      i = @frequency[key]
      @rentused[i].delete(key)
      @rentused[i + 1] = { key => nil } if @rentused[i + 1].nil?
      @rentused[i + 1][key] = nil
      @frequency[key] += 1
      # p @cache, @frequency, @rentused
      @cache[key]
    else
      -1
    end
  end

  #     :type key: Integer
  #     :type value: Integer
  #     :rtype: Void
  def put(key, value)
  	return if @capacity.zero?
    if @cache.key?(key) || !@cache.key?(key) && @cache.size < @capacity
      @cache[key] = value
      @frequency[key] += 1
      i = @frequency[key]
      if i == 1 # a new item
        @rentused[1] = { key => nil } if @rentused[1].nil?
        @rentused[1][key] = nil
      else
        @rentused[i - 1].delete(key)
        @rentused[i] = { key => nil } if @rentused[i].nil?
        @rentused[i][key] = nil
      end
    else
      1.upto(100).each do |i|
        next unless !@rentused[i].nil? && !@rentused[i].empty?
        k = @rentused[i].keys.first
        @cache.delete(k)
        @frequency.delete(k)
        @rentused[i].delete(k)
        break
      end
      @cache[key] = value
      @frequency[key] = 1
      @rentused[1] = { key => nil } if @rentused[1].nil?
      @rentused[1][key] = nil
      # p @cache, @frequency, @rentused
    end
  end
end

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache.new(1)
obj.put(2, 1)
p obj.get(2)
obj.put(3, 2)
p obj.get(2)
exit

obj.put(1, 1)
obj.put(2, 2)
p obj.get(1)
obj.put(3, 3)
p obj.get(2)
p obj.get(3)
obj.put(4, 4)
p obj.get(1)
p obj.get(3)
p obj.get(4)




