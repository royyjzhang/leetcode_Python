class Solution(object):
    mapping={"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":" "}
    def __init__(self):
        self.result=[]        
        self.substring=""
    def search(self,digits,index):
        if (index==len(digits)):
            self.result.append(self.substring)
            return
        char=digits[index]
        temp=Solution.mapping[char]
        for i in temp:
            self.substring+=i
            self.search(digits,index+1)
            self.substring=self.substring[:-1]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (len(digits)==0):
            return self.result
        index=0
        self.search(digits,index)
        return self.result

digits="23"
solution=Solution()
print solution.letterCombinations(digits)
