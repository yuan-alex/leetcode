class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.store = []

    def next(self, val: int) -> float:
        if len(self.store) == self.size:
            self.store.pop(0)
        self.store.append(val)
        return sum(self.store) / len(self.store)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
