class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                totalSum = nums[left] + nums[right] + a

                if totalSum > 0:
                    right -= 1
                elif totalSum < 0:
                    left += 1
                else:
                    result.append([nums[left], nums[right], a])
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
            
        return result