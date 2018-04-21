class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lastWidth = 0
        lines = 1
        for c in S:
            if lastWidth + widths[ord(c) - ord('a')] > 100:
                lines += 1
                lastWidth = 0
            lastWidth += widths[ord(c) - ord('a')]
        return [lines, lastWidth]

def main():
    solution = Solution()
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print(solution.numberOfLines(widths, S))

if __name__ == "__main__":
    main()

