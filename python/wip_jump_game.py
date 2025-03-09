# Not Working

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        end_index = len(nums)
        jumps = nums[0]
        if end_index == jumps:
            return Tru
        possible_next_jumps = []
        for i in range(jumps):
            possible_next_jumps.append(nums[i])
        if end_index in possible_next_jumps:
            return True

        possible_third_jump= []
        for jump in possible_next_jumps:
            for i in range(jumps):
                possible_third_jump.appemd
        return False


