class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]
        results = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num, count in counts.items():
            frequency[count].append(num)
        
        for i in range(len(frequency) - 1, -1, -1):
            for elem in frequency[i]:
                results.append(elem)
                if len(results) == k:
                    return results


