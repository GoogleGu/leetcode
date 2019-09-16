public class SolutionZcsh {
    /**
     * 实现原理, num1 与 num2 , 非, 且运算; 每做一次, 且运算的结果左移一位
     * @param num1
     * @param num2
     * @return
     */
    public int Add(int num1,int num2) {
        int reuslt = num1 ^ num2;
        for (int fei = reuslt, qie = num1 & num2; qie != 0; reuslt = fei) {
            qie = qie << 1;
            int tempFei = fei ^ qie;
            qie = fei & qie;
            fei = tempFei;
        }
        return reuslt;
    }
}
