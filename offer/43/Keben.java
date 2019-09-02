public class Solution {
    public String LeftRotateString(String str,int n) {
        if(str.length()<1){
            return "";
        }
        String left = str.substring(0,n);
        String right = str.substring(n);
        return right +left;
    }
}
