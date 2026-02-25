class Solution:
    def longestPalindrome(self, s: str) -> str:
        # self.res = ""

        # def find(i, j, s):
        #     if j == len(s):
        #         return

        #     curr_str = s[i:j+1]

        #     if curr_str == curr_str[::-1]:
        #         if len(self.res) < len(curr_str):
        #             self.res = curr_str

        #     find(i, j + 1, s)

        # n = len(s)
        # for i in range(len(s)):
        #     find(i, i, s)

        # return self.res

        res = ""
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(res):
                    res = s[left:right + 1]

                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(res):
                    res = s[left:right + 1]

                left -= 1
                right += 1

        return res
            

