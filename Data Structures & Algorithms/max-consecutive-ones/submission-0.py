class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0
            max_consecutive = max(max_consecutive, current_count)
        return max_consecutive