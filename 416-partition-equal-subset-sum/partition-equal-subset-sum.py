class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Space optimization
        if(len(nums)) == 1 and sum(nums) % 2 == 0:
            return False
        
        if sum(nums) % 2 != 0:
            return False
        
        m = (sum(nums) // 2) + 1

        prev = [False for _ in range(m)]
        prev[0] = True

        if nums[0] < m: prev[nums[0]] = True

        for i in range(1, len(nums)):
            curr = [False for _ in range(m)]
            for j in range(1, m):
                target = j
                # do stuffs
                num = nums[i]

                pick = None
                if (nums[i] <= target): 
                    pick = prev[target - num]
                
                not_pick = prev[target]
                curr[target] = pick or not_pick
            
            prev = curr
        

        return prev[sum(nums) // 2]