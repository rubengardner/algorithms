from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        order = {i: nums.count(i) for i in set(nums)}
        max_key = 0
        max_value = 0
        for key, value in order.items():
            if max_value < value:
                max_value = value
                max_key = key
        return max_key
