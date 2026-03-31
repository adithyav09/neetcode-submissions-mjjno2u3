class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output_lst = []
        i = 0
        while i < 2:
            for j in range(len(nums)):
                output_lst.append(nums[j])
            i += 1
        return output_lst
    