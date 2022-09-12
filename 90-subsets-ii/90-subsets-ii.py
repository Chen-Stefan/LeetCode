class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums:
            return results
        
        nums.sort()
        subset = []
        self.dfs(nums, 0, subset, results)
        return results
    
    def dfs(self, nums, startIndex, subset, results):
        # deepcopy subset and add to results
        results.append(subset[:])
        
        for index in range(startIndex, len(nums)):
            if (index != 0 and nums[index] == nums[index - 1] and index > startIndex):
                continue
            subset.append(nums[index])
            # index + 1是去重 (1, 2) 和 (2, 1)
            self.dfs(nums, index + 1, subset, results)
            subset.pop(len(subset) - 1)
        
    
        

            