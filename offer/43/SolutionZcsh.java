public class SolutionZcsh {
    public String LeftRotateString(String str,int n) {
        if (str == null || str.length() == 0) {
            return str;
        }
        int number = n % str.length();
        return str.substring(number)  + str.substring(0,number);
    }
}
