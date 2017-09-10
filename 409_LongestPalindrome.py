class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        checked={}
        result=0
        singleflag=False
        for char in s:
        	if (char not in checked):
        		checked[char]=1
        	else:
        		checked[char]=checked[char]+1
        #print checked
        allchar=checked.keys()
        #print allchar
        for char in allchar:
            if ((checked[char]%2==1) and (not singleflag)):
                result=result+int(checked[char]/2)*2+1
                singleflag=True
            else:
                result=result+int(checked[char]/2)*2
        return result

solution=Solution()
s='abccccdd'
result=solution.longestPalindrome(s)
print result
