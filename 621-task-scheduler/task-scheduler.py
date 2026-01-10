class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]

        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while maxHeap or q:
            # with each process increment time
            time += 1

            if maxHeap:
                count = 0 - heapq.heappop(maxHeap)
                count -= 1
                if count > 0:
                    # Decrement it by one
                    q.append([-count, time + n])
            
            # are we done with idle/interval time
            if q and q[0][1] == time:
                # add back time to maxHeap to be processed.
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
