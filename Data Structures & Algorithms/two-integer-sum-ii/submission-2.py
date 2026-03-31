class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            if target == numbers[p1] + numbers[p2]:
                return [p1 + 1, p2 + 1]
            elif target > numbers[p1] + numbers[p2]:
                p1 += 1
            elif target < numbers[p1] + numbers[p2]:
                p2 -= 1
        return []
