class Foo:
    def __init__(self):
        self.orders = [0, 0, 0, 0]


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        self.orders[0] = printFirst
        self.orders[3] += 1
        self.exec()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.orders[1] = printSecond
        self.orders[3] += 1
        self.exec()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.orders[2] = printThird
        self.orders[3] += 1
        self.exec()

    
    def exec(self):
        if self.orders[3] == 3:
            self.orders[0]()
            self.orders[1]()
            self.orders[2]()
            
