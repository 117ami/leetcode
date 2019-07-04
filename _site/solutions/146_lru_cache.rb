class LRUCache
  #     :type capacity: Integer
  def initialize(capacity)
    @capacity = capacity
    @cache = {}
  end

  #     :type key: Integer
  #     :rtype: Integer
  def get(key)
    return -1 unless @cache.key?(key)
    val = @cache[key]
    @cache.delete(key)
    @cache[key] = val
    val
  end

  #     :type key: Integer
  #     :type value: Integer
  #     :rtype: Void
  def put(key, value)
    return if @capacity.zero?
    @cache.delete(key)
    @cache.shift while @cache.size >= @capacity
    @cache[key] = value
  end
end

# Your LFUCache object will be instantiated and called as such:
obj = LRUCache.new(2)
obj.put(1, 1)
obj.put(2, 2)
p obj.get(1)
obj.put(3, 3)
p obj.get(2)
obj.put(4, 4)
p obj.get(1)
p obj.get(3)
p obj.get(4)
