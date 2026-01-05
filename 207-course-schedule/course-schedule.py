class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph
        graph = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            graph[a].append(b)

        # We will have these states.
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # List to hold the states for all the nodes.

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            # Base case
            if state == VISITING:
                return False
            if state == VISITED:
                return True
            
            # mark the curr course node as visiting i.e. it's being seen right now
            states[node] = VISITING
            # Go through all the course neighbours
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            # means we have verified we can take this course
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        