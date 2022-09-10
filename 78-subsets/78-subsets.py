class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        if not nums:
            return results
        nums.sort()
        self.dfs(nums, 0, subset, results)
        return results
        
    def dfs(self, nums, index, subset, results):
        # 递归的出口
        if index == len(nums):
            results.append(copy.deepcopy(subset))
            return 
        # 递归的拆解
        # 选nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, results)
        
        # 选nums[index]
        subset.pop(len(subset) - 1)
        self.dfs(nums, index + 1, subset, results)