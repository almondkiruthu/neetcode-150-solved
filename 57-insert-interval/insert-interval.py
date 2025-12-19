import copy

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # No need to modify the intervals array in place, create a new intervals array
        # and then perform the merge.
        new_intervals = copy.copy(intervals)
        new_intervals.append(newInterval)
        new_intervals.sort(key = lambda interval: interval[0])

        merged = []

        for i in range(len(new_intervals)):
            interval = new_intervals[i]

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]

        
        return merged
        