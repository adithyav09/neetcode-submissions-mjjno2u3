class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        
        for num, count in hashmap.items():
            frequency[count].append(num)
        
        result = []
        for i in range(len(frequency) - 1, -1, -1):
            for elems in frequency[i]:
                if len(result) < k:
                    result.append(elems)
        return result


