public class SolutionZcsh {
    int index = 0;

    public boolean isNumeric(char[] str) {

        if (str.length == 0) {
            return false;
        }

        boolean isNumber = isNumber(str, false);
        if (str.length > index && str[index] == '.') {
            index++;
            isNumber = isNumber(str, true);
        }
        if (str.length > index && (str[index] == 'E' || str[index] == 'e')) {
            index++;
            isNumber = isNumber(str, false);
        }
        return isNumber && index == str.length;
    }

    public boolean isNumber(char[] str, boolean isUnsigned) {

        if (index < str.length && !isUnsigned) {
            index = str[index] == '+' || str[index] == '-' ? ++index : index;
        }
        int initValue = index;
        while (index < str.length && str[index] >= '0' && str[index] <= '9') {
            index++;
        }
        return index != initValue;
    }
}
