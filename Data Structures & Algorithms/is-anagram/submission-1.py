class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for char in t:
            count[char] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True