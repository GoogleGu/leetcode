
class Solution:

    solutions = [0, 1, 2]

    def rect_cover(self, number):
        if number >= len(self.solutions):
            self.extend_solutions_till(number)
        return self.solutions[number]

    def extend_solutions_till(self, number):
        current_index = len(self.solutions)
        while current_index <= number+1:
            self.solutions.append(self.solutions[current_index-2] + self.solutions[current_index-1])
            current_index += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.rect_cover(6))
