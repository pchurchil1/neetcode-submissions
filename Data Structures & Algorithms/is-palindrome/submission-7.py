class Solution:
    # Input: String s
    # Output: Boolean value isPalindrome
    def isPalindrome(self, s: str) -> bool:
        sString = ""
        for c in s:
            if c.isalnum():
                sString += c.lower()

        l, r = 0, len(sString)-1

        while l < r:
            if sString[l] != sString[r]:
                return False
            l+=1
            r-=1
        return True

