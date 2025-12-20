class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Note that intervals with equal end and start are considered non-overlapping
        def sort_by_interval_start(interval):
            return interval[0]
        intervals.sort(key = sort_by_interval_start)
        merged = []
        overlap_count = 0
        for i in range(len(intervals)):
            interval = intervals[i]
            if not merged or merged[-1][1] <= interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals, it helps us understand the maximum n.o
                # of overlapping intervals we can have hence 
                # len(intervals) - len(merged) == n.o of overlapping intervals removed.
                merged[-1] = [merged[-1][0], min(merged[-1][1], interval[1])]
        
        return len(intervals) - len(merged)
        