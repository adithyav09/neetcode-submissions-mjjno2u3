class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Create two pointers one starting at the beginning of the array and the other at the end.
        # While the left pointer is less than the right pointer iterate through the array.
        # Define the mid point of the array (L + R // 2).
        # if midpoint is equal to the target return index of midpoint.
        # If target is greater than midpoint, move left pointer to be equal to the right of midpoint.
        # If target is less than midpoint, move right pointer to be equal to left of the midpoint.
        '''
        [1, 2, 3, 4, 5], target = 4
         L     M      R
        ''' 
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1