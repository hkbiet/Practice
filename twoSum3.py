class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for index, item in enumerate(nums):
            diff = target - item
            if diff in store:
                return [store[diff],index]
            store[item] = index
