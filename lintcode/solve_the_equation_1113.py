# author: Arthur
# date: 2019.1.14


class Solution:

    @staticmethod
    def solveEquation(equation):
        x_index = 0
        constant = 0

        def parse_text(text):
            nonlocal x_index
            nonlocal constant
            if not text:
                return
            if 'x' in text:
                if len(text) == 1:
                    x_index += over * sign * 1
                else:
                    x_index += over * sign * eval(text[:-1])
            else:
                constant += over * sign * eval(text)

        # 解析式子
        start = 0
        over = -1
        sign = 1
        for i, char in enumerate(equation+'+'):
            if char == '+':
                parse_text(equation[start:i])
                start = i + 1
                sign = 1
            elif char == '-':
                parse_text(equation[start:i])
                start = i + 1
                sign = -1
            elif char == '=':
                parse_text(equation[start:i])
                start = i + 1
                sign = 1
                over = 1

        # 解析结果
        if x_index == 0 and constant == 0:
            return 'Infinite solutions'
        elif x_index == 0 and constant != 0:
            return "No solution"
        else:
            return 'x={}'.format(int(-constant / x_index))

if __name__ == '__main__':
    print(Solution.solveEquation("1-x+x-x+x+2x=-99-x+x-x+x"))
