class Solution:

    def power(self, base, exponent):
        if exponent < 0:
            return 1/self.positive_power(base, -exponent)
        else:
            return self.positive_power(base, exponent)

    @staticmethod
    def positive_power(base, exponent):
        power = 1
        for exp_i in range(exponent):
            power *= base
        return power
