class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            graph[a].append(b)

        # We will have these states.
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        order = []

        def dfs(node):
            state = states[node]
            if state == VISITING:
                return False
            if state == VISITED:
                return True

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order
