class Solution(object):
    def backtrack(self, nums, index, current, all_subsets):
        if index == len(nums):
            all_subsets.append(current[:])  # Add a copy of current subset
            return
        current.append(nums[index])
        self.backtrack(nums, index + 1, current, all_subsets)
        current.pop()
        self.backtrack(nums, index + 1, current, all_subsets)

    def subsets(self, nums):
        all_subsets = []
        self.backtrack(nums, 0, [], all_subsets)
        return all_subsets
solution = Solution()
nums = [1, 2, 3]
result = solution.subsets(nums)
print(result)  