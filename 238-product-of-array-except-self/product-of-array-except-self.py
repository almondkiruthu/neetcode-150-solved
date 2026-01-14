class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [0] * n
        right_arr = [0] * n
        res = [0] * n

        for i in range(n):
            if i == 0:
                left_arr[i] = 1
            else:
                left_arr[i] = left_arr[i - 1] * nums[i - 1]

        for j in range(n - 1, -1, -1):
            if j == n - 1:
                right_arr[j] = 1
            else:
                right_arr[j] = right_arr[j + 1] * nums[j + 1]

        for k in range(n):
            res[k] = left_arr[k] * right_arr[k]

        return res