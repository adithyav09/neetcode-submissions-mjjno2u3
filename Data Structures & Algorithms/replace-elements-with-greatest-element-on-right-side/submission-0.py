class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Create a for loop to iterate through the array
        # Create a variable right_largest to keep track of the largest number to the right
        # Create a nested for loop that iterates the remaining numbers in the array
        # While iterating, update the right_largest variable with the max largest number to the right of current index
        # Come out of nested for loop and then update current index with right_largest value
        # Come out of outer for loop and replace last index with -1

        for i in range(len(arr)):
            right_largest = 0
            for j in range(i + 1, len(arr)):
                right_largest = max(right_largest, arr[j])
            arr[i] = right_largest
        arr[-1] = -1
        return arr