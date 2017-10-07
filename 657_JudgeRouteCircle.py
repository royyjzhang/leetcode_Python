class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for instruction in moves:
            if instruction == 'U':
                y+=1
            elif instruction == 'D':
                y-=1
            elif instruction == 'L':
                x-=1
            elif instruction == 'R':
                x+=1
        return (x == 0 and y == 0)
        
def main():
    solution = Solution()
    moves = "LL"
    print(solution.judgeCircle(moves))

if __name__=="__main__":
    main()