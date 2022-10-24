class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return 
        temp = [0 for _ in range(m + n)]
        first_index, second_index, temp_index = 0, 0, 0         
        while first_index <= m - 1 and second_index <= n - 1:
            if nums1[first_index] <= nums2[second_index]:
                temp[temp_index] = nums1[first_index]
                temp_index += 1
                first_index += 1
            else:
                temp[temp_index] = nums2[second_index]
                temp_index += 1
                second_index += 1
        
        while first_index <= m - 1:
            temp[temp_index] = nums1[first_index]
            first_index += 1
            temp_index += 1
        while second_index <= n - 1:
            temp[temp_index] = nums2[second_index]
            second_index += 1
            temp_index += 1
        
        for index in range(m + n):
            nums1[index] = temp[index]
            
                