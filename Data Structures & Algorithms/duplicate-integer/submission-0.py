class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # empty set
        # for each number in nums:
        #   if each number is already in set:
        #       stop the loop and say yes
        #   else:
        #      add number to the set
        # say no duplicates if loop reaches the end of array.
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

