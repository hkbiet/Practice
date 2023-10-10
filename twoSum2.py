class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reserve = []
        for i in range(len(nums)):
            if target-nums[i] in reserve:
                return [i, nums.index(target-nums[i])]
            else:
                reserve.append(nums[i])