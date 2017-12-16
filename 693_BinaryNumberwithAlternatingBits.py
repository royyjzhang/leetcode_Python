class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True
        current = 1
        while current < n:
            if flag:
                current = current << 1
                flag = False
            else:
                current = (current << 1) + 1
                flag = True
        if current == n:
            return True
        else:
            return False

def main():
    solution = Solution()
    n = 10
    print(solution.hasAlternatingBits(n))

if __name__=="__main__":
    main()