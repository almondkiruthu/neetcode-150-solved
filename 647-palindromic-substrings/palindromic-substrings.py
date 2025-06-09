class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0
        for i in range(len(s)):
            # odd length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # expand from the current character as the center of the palindrome.
                palindrome_count += 1
                left -= 1
                right += 1
            # even length palindromes.
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome_count += 1
                # expand from the current character as the center of the palindrome.
                left -= 1
                right += 1
        
        return palindrome_count

        