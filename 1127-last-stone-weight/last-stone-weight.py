import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        # Now we we have our maxHeap.
        while len(maxHeap) > 1:
            # that means I can keep picking two.
            # steps to conduct.
            weight_y = -heapq.heappop(maxHeap)
            weight_x = -heapq.heappop(maxHeap)

            if weight_y != weight_x:
                # simply means x is greater.
                heapq.heappush(maxHeap, -(weight_y - weight_x))
            
            # else push nothing both are destroyed.

        if len(maxHeap) == 0:
            return 0
        
        return -maxHeap[0]

