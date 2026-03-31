class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i, num in enumerate(nums):
            dictionary[num] = i
        
        for i, num in enumerate(nums):
            result = target - num
            if result in dictionary and dictionary[result] != i:
                return [i, dictionary[result]]
        return []