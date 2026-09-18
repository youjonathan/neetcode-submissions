class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 == 1:
            return self.arr[int(len(self.arr) / 2)]
        return (self.arr[int(len(self.arr) / 2)] + self.arr[int(len(self.arr) / 2) - 1]) / 2