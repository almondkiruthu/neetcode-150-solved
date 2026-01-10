import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # the dict to hold the weight:
        least_cost = {}    
        # Build the adjacency list graph
        graph = defaultdict(list)
        for src, dest, weight in times:
            graph[src].append((dest, weight))
            # uncomment if it's undirected.
            # graph[dest].append((src, weight))

        # source cost and node
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        
        while minHeap:
            # we pop the node and the cost to reach that node.
            cost, node = heapq.heappop(minHeap)
            # if we found shortest path for a specific node skip it.
            if node in least_cost:
                continue
            least_cost[node] = cost
            # we then explore all it's neighbours.
            for nei in graph[node]:
                nei_node, nei_weight = nei
                if nei_node not in least_cost:
                    new_cost = cost + nei_weight
                    heapq.heappush(minHeap, (new_cost, nei_node))

        if len(least_cost) != n:
            return -1
        
        return max(least_cost.values())
        
        