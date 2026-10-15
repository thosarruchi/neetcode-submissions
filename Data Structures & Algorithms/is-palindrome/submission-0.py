class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        print(new)
        i = 0
        j = len(new) - 1
        while i < j:
            if new[i] == new[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        







        