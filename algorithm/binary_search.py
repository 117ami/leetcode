

class BS:
    '''General template for binary search 
    '''
    def search(lv: int, rv: int, bool_func):
        left, right = lv, rv
        while left < right:
            mid = (left + right) // 2
            if bool_func(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
