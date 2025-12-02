class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        # To record the counts of each character
        A = [0] * 26
        for r in range(len(s)):
            char = s[r]
            A[(ord(char) - 65)] += 1
            changes_required = ((r - l) + 1)  - max(A)
            if changes_required > k:
                left_char = s[l]
                A[(ord(left_char) - 65)] -= 1
                l += 1
            window_size = r - l + 1
            longest = max(longest, window_size)

        return longest


        