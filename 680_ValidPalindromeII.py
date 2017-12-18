class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while (left < right):
            if (s[left] != s[right]):
                return (self.checkPalindrome(s[left:right]) or self.checkPalindrome(s[left + 1:right + 1]))
            left += 1
            right -= 1
        return True

    def checkPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while(left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

def main():
    solution = Solution()
    s = 'deeee'
    print(solution.validPalindrome(s))

if __name__=="__main__":
    main()