class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort in place
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # If what we are looking at is greater than zero then we are sure it's going
            # to yield to higher sums skip it, end our loop
            if nums[i] > 0:
                break
            # Make sure we don't start on the same offset
            if i > 0 and nums[i] == nums[i - 1]:
                # skip continue
                continue
            low = i + 1
            high = n - 1
            while low < high:
                # Process the sum
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    # Now move the two pointer low and high over our range.
                    low += 1
                    high -= 1
                    # Make sure we don't process a triplet group we have seen before
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    # Note that high is moving in reverse
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif curr_sum < 0:
                    low += 1
                else:
                    high -= 1

        return res
