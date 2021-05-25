import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_lo = []
        self.min_hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_lo,(-num,num))
        _,max_lo_balanced = heapq.heapop(self.max_lo)
        heapq.heappush(self.min_hi,max_lo_balanced)

        if len(self.max_lo) < len((self.min_hi)):
            min_hi_balanced = heapq.heappop(self.min_hi)
            heapq.heappush(self.max_lo,(-min_hi_balanced,min_hi_balanced))

    def findMedian(self) -> float:
        if (len(self.max_lo)+len(self.min_hi)) % 2 == 0:
            return  (self.max_lo[0][1] + self.min_hi[0]) // 2
        else:
            return self.max_lo[0][1]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

print(3//2)
