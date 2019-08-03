

class H2O:
    def __init__(self):
        self.hy, self.ox = deque(), deque()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hy.append(releaseHydrogen)
        self.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.ox.append(releaseOxygen)
        self.release()
    
    def release(self):
        if len(self.hy) >= 2 and len(self.ox) >= 1:
            self.hy.popleft()()
            self.hy.popleft()()
            self.ox.popleft()()
