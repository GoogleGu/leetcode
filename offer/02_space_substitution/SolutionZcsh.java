public class Solution {
    public String replaceSpace(StringBuffer str) {
        int blankCount = 0;
        for (int i = 0; i < str.length(); i++){
            if (str.charAt(i) == ' '){
                blankCount++;
            }
        }
        
        int originalLength = str.length();
        str.setLength(str.length() + blankCount * 2);
        int index = str.length() - 1;
        for (int i = originalLength - 1; i >= 0; i--){
            if (str.charAt(i) == ' ') {
                str.setCharAt(index--,'0');
                str.setCharAt(index--,'2');
                str.setCharAt(index--,'%');
            } else {
                str.setCharAt(index--,str.charAt(i));
            }
        }
        return str.toString();
    }

}
