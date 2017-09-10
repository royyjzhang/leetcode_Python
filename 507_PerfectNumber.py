import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0) or (num == 1):
            return False
        divider_sum = 1
        for i in range(1, int(math.sqrt(num)) + 1):
            if (num % i == 0) and (i != 1):
                divider_sum = divider_sum + i + (num / i)
        if (num  == divider_sum):
            return True
        else:
            return False

def main():
    solution = Solution()
    num = 6
    print solution.checkPerfectNumber(num)

if __name__ == "__main__":
    main()
