class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> temp (m + n, 0);
        int first_index = 0, second_index = 0, temp_index = 0;      
        while (first_index <= m - 1 && second_index <= n - 1) 
        {
            if (nums1[first_index] <= nums2[second_index]) 
            {   
                temp[temp_index++] = nums1[first_index++];
            }
            else
            {
                temp[temp_index++] = nums2[second_index++];
            }
        }
        
        while (first_index <= m - 1)
        {
            temp[temp_index++] = nums1[first_index++];
        }
        while (second_index <= n - 1)
        {
            temp[temp_index++] = nums2[second_index++];
        }
        int index = 0;
        for (int val : temp)
        {
            nums1[index++] = val;
        }
    }
};