class Solution:
    def Power(self, base, exponent):
        ## 幂的运算  2^2 * 2^3 = 2^5
        ## 5 -> 0101
        ## 0100 = 4
        ## 0001 = 1
        ## 15 -> 1111
        ## 1000 -> 8
        ## 0100 -> 4
        ## 0010 -> 2 -> >>1 -> 0001 > base*1
        ## 0001 -> 1 -> base*1
        if exponent == 0:
            return 1
        res = 1
        opt_value = base
        opt_exponent = exponent
        if exponent < 0:
            opt_exponent = -exponent
        ## 2^5 -> 0010^0101
        ## 指数>>1后
        ## 0010^0100 -> 2^4
        ## 0100^0010  -> 4^2
        while opt_exponent > 0:
            if opt_exponent & 1 == 1:
                res *= opt_value
            ## 整数直接位移：opt_value << 1
            opt_value *= opt_value
            opt_exponent = opt_exponent >> 1
        return res if exponent > 0 else 1 / res


print(Solution().Power(2, -3))
