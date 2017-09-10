class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 9
        digits = 1
        while (n - base * digits > 0):
            n -= base * digits
            base *= 10
            digits += 1
        index = n % digits
        if (index == 0):
            index = digits
        num = 10 ** (digits - 1)
        if (index == digits):
            num += n / digits - 1
        else:
            num += n / digits
        for i in range (index, digits):
            num /= 10
        return num % 10

def main():
    solution = Solution()
    n = 3
    print solution.findNthDigit(n)

if __name__ == "__main__":
    main()
