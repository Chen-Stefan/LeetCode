class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        if not nums:
            return results
        nums.sort()
        self.dfs(nums, 0, subset, results)
        return results
        
    def dfs(self, nums, startIndex, subset, results):
        results.append(copy.deepcopy(subset))
        for index in range(startIndex, len(nums)):
            subset.append(nums[index])
            self.dfs(nums, index + 1, subset, results)
            subset.pop(len(subset) - 1)
    
        