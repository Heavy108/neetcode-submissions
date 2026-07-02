class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_text = list(s)
        second_text = list(t)
        for i in range(0, len(s)):
            if first_text[i] in second_text:
                second_text.remove(first_text[i])
            else:
                return False
        return True

        