class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product_output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            product_output[i] *= postfix
            postfix *= nums[i]

        return product_output 