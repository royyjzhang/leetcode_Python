# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

SET_NUM = 6
def guess(num):
    if (num < SET_NUM):
        return 1
    elif (num > SET_NUM):
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while (start < end):
            mid = int((start + end) / 2)
            if (guess(mid) == 0):
                return mid
            elif (guess(mid) == 1):
                start = mid + 1
            else:
                end = mid
        return start

def main():
    solution = Solution()
    n = 10
    print solution.guessNumber(n)

if __name__ == "__main__":
    main()
