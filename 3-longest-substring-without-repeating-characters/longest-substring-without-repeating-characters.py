class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        _set = set()
        max_length = 0

        for windowEnd in range(len(s)):
            # Else if it's already in the set.
            # We want to continously shrink our window by removing the already present
            # elements from the left.
            while s[windowEnd] in _set:
                _set.remove(s[windowStart])
                windowStart += 1
            
            # If not in our set build our set and update the length
            window = windowEnd - windowStart + 1
            max_length = max(max_length, window)

            #Add the element to the set.
            _set.add(s[windowEnd])
        return max_length