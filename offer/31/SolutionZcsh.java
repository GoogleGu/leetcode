public class Solution {
    public int NumberOf1Between1AndN_Solution(int n) {
        int sum = 0;
        int i = 1;
        while (n >= i) {
            // 当前位的改变次数
            int changeNumber = n / i;
            // 剩余的改变次数,即未满一圈的次数 ,如 21, 在遍历到 十位时, residueChangeNumber 就是 1
            int residueChangeNumber = n % i;

            // 所有满圈的 1 的个数
            int yiQuanShu = changeNumber / 10  * i;

            // 当前位,未满一圈的数字 ,如 21, 在遍历到 十位时, residueChangeNumber 就是 2
            int weiManYiQuan = changeNumber % 10;

            // 判断当前未满一圈的数字是否大于 1 或者等于 1
            // 加上未满一圈出现的 1 的次数
            if (weiManYiQuan > 1) {
                sum += i;
            } else if (weiManYiQuan == 1) {
                sum += residueChangeNumber + 1;
            }
            // 加上所有满一圈出现的次数
            sum += yiQuanShu;
            i *= 10;
        }

        return sum;
    }
}
