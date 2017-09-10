import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.floor((-1 + math.sqrt(4 * 2 * n + 1)) / 2))

def main():
    solution = Solution()
    n = 5
    print solution.arrangeCoins(n)

if __name__ == "__main__":
    main()
