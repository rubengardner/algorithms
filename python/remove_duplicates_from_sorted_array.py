from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        order = {i: 0 for i in nums}
        for i in nums:
            order[i] += 1

        for key, value in order.items():
            if value > 2:
                number_of_exceding_int = value - 2
                for i in range(number_of_exceding_int):
                    nums.remove(key)
        return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
a = Solution().removeDuplicates(nums=nums)
print(nums)
print(a)