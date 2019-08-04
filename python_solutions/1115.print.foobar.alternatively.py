
from collections import deque
class FooBar:
    def __init__(self, n):
        self.n = n
        self.orders = deque()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for _ in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.orders.appendleft(printFoo)
        
        self.exec()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for _ in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.orders.append(printBar)
        self.exec()

    
    def exec(self):
        if len(self.orders) == self.n * 2:
            for _ in range(self.n):
                self.orders.popleft()()
                self.orders.pop()()
