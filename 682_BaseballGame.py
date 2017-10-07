class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = 0
        stack = []
        for instruction in ops:
            if instruction == "C" and stack:
                last = stack.pop()
                result -= last
            elif instruction == "D" and stack:
                result += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif instruction == "+" and len(stack) > 1:
                result += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                result += int(instruction)
                stack.append(int(instruction))
        return result

def main():
    solution = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    print(solution.calPoints(ops))

if __name__=="__main__":
    main()