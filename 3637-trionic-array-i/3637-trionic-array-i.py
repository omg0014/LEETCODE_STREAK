class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        c = 0
        for i in range(1, len(nums)):
            a = nums[i-1]

            if a == nums[i]:
                return False

            if c == 0:
                if a > nums[i]:
                    if i == 1:         
                        return False
                    c += 1

            elif c == 1:
                if a < nums[i]:
                    c += 1

            elif c == 2:
                if a > nums[i]:
                    return False

            else:
                return False

        return c == 2
