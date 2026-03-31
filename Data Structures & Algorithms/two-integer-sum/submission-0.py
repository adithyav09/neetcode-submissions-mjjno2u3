class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: I will use two for loops, one fast and one slow. The slow will sum the ith index integer with the jth (fast) index integer. Both are distinct indices. If bos of distinct indices add up to sum will return those indices. There is a guarantee based on problem that there will be atleast 2.
        # Pseudocode:
        # for each index i from 0 to length of nums - 1:
        #   for each index j from 0 to length of nums - 1:
        #       if i is not j:
        #           if element at index i + element at index j = target:
        #               return [i, j]
        # return empty array (will not be reached)
        # Complexity: Time O(N^2), Space O(1)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []
        