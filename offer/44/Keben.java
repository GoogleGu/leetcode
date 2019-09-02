public class Solution {
        public static String ReverseSentence(String str) {
         if(str.trim().equals("")){
            return str;
        }
        String[] temp = str.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = temp.length-1; i >= 0; i--) {
            sb.append(temp[i]).append(" ");
        }
        return sb.toString().trim();
    }
}
