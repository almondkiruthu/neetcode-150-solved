class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []

        # add all numbers into our minheap
        for num in nums:
            self.add(num)      

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minheap, val)

        # keep a minheap of window size or capacity k
        # no matter how many elements added previously, we are sure we have k elements 
        # sorted in some manner.
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)