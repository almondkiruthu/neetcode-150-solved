class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        height = {}
        par = {}
        # Implementing union find to find if there's a cycle.
        # 1. First intialize every course to be independent i.e. a parent of itself.

        for i in range(1, len(edges) + 1):
            height[i] = 0
            par[i] = i

        # 2. Impelementing the find operation for the union find.
        def find(course):
            # initalize parent
            p = par[course]

            # iterate until we find a parent that's equal to itself meaning we have found
            # a source/root of the disjoint subset.
            while p != par[p]:
                p = par[p]

            return p

        # 3. Implementing the union operation for the union-find algorithm
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)

            if p1 == p2:
                return False

            if height[p1] > height[p2]:
                par[p2] = p1
            elif height[p1] < height[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                height[p1] += 1

            return True

        cycle_edges = []

        for n1, n2 in edges:
            satisfied_conn = union(n1, n2)

            if not satisfied_conn:
                cycle_edges.append([n1, n2])

        if len(cycle_edges) > 1:
            return cycle_edges[-1]
        elif len(cycle_edges) == 1:
            return cycle_edges.pop()
        else:
            return []
