class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length_of_array = len(nums)
        ordering_array = [0 for i in range(length_of_array)]
        if k > length_of_array:
            k = k % length_of_array
        for i in range(length_of_array):
            index = (i + k) - length_of_array
            ordering_array[index] = nums[i]
        for i in range(length_of_array):
            nums[i] = ordering_array[i]

# nums = [1,2,3,4,5,6,7]
# Solution().rotate(nums=nums, k=2)
# print(nums) # [5,6,7,1,2,3,4]

nums = [-1]
Solution().rotate(nums=nums, k=2)
print(nums)  #[3,99,-1,-100]


