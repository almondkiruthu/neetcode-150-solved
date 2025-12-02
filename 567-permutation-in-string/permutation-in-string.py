class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sig = Counter(s1)
        k = len(s1)

        windowStart = 0
        s2_sig = {}
        for windowEnd in range(len(s2)):
            # Build our current signature so far.
            right_char = s2[windowEnd]
            if right_char not in s2_sig:
                s2_sig[right_char] = 1
            else:
                s2_sig[right_char] += 1
            
            # If the current window is greater than K reduce it from the left
            # The signature formed will always be greater than the signature of s1.
            if windowEnd - windowStart + 1 > k:
                left_char = s2[windowStart]
                s2_sig[left_char] -= 1
                if s2_sig[left_char] == 0:
                    del s2_sig[left_char]
                
                windowStart += 1

            
            if s1_sig == s2_sig:
                return True
        
        return False
        