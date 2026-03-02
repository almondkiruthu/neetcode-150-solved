class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_substrings(i):
            if i >= len(s):
                return 0

            local_count = 0
            for j in range(i, len(s)):
                curr_str = s[i:j + 1]
                if curr_str == curr_str[::-1]:
                    local_count += 1

            
            return local_count + count_substrings(i + 1)
        
        return count_substrings(0)

