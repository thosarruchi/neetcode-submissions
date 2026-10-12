class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        longest = -1
        for i, char in enumerate(s):
            if char in seen:
                length = i - seen[char] - 1
                longest = max(longest, length)
            else:
                seen[char] = i
        return longest

       
            

        