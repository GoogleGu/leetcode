public class Solution {
    public double Power(double base, int exponent) {
        double temp = exponent;
        if (exponent == 0){
            return 1;
        } else if (exponent < 0) {
            if (base == 0) {
                throw new RuntimeException("分母为0");
            }
            exponent = -exponent;
        }

        double tag = 1;
        while (exponent != 0) {
            if ((exponent & 1) == 1){
                tag *= base;
            }
            base *= base;
            exponent = exponent >> 1;
        }
        return temp < 0 ? 1/tag : tag;
  }
}
