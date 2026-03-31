class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_string = ""
        for char in s:
            if char.isalnum():
                output_string += char.lower()
        p1 = 0
        p2 = len(output_string) - 1
        while p1 < p2:
            if output_string[p1] != output_string[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

