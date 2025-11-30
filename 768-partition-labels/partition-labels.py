class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Build the last_index_occurrence_for_each char
        last_index_map = {}
        for i, char in enumerate(s):
            last_index_map[char] = max(i, last_index_map.get(char, 0))

        end = 0
        size = 0
        res = []

        # Iterate through the characters and build, until i == end.
        # That forms our partition and then reset size.
        for i, char in enumerate(s):
            end = max(end, last_index_map.get(char))
            size += 1
            if i == end:
                res.append(size)
                size = 0
        
        return res

            

        