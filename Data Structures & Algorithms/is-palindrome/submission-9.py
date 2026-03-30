class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string 
        
        
        alphanumeric = string.ascii_letters + string.digits
        s = "".join(char for char in s if char in alphanumeric and char != " ").lower()
        
        if len(s) ==0:
            return True
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -=1
                if left >= right:
                    return True
                
            else: 
                return False

            