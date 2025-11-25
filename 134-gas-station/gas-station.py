class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            # if by any chance our total falls below zero we know we need to start in
            # the next position.
            if total < 0:
                total = 0
                start = i + 1
        # we guranteed that we return start our starting point will be positive
        # moving forward.
        return start