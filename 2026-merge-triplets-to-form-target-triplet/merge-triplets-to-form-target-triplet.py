import copy

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()

        for triplet in triplets:
            # Skip all values that are greater than our target values.
            if (triplet[0] > target[0] or 
                triplet[1] > target[1] or
                triplet[2] > target[2]):
                    continue

            # For each triplet value, check if it's equal and it's position aligns
            # With the target object then add that index to the set to account
            # for duplicates.
            for i, val in enumerate(triplet):
                if val == target[i]:
                    res.add(i)

        return len(res) == len(target)
        