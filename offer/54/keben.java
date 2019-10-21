public class Solution {
    //Insert one char from stringstream
    private StringBuilder sb = new StringBuilder();

    private int[] hash = new int[256];

    public void Insert(char ch) {
        sb.append(ch);
        hash[ch]++;
    }
    //return the first appearence once char in current stringstream
    public char FirstAppearingOnce() {
        for (int i = 0; i < sb.length(); i++) {
            char s = sb.charAt(i);
            if (hash[s]==1){
                return s;
            }
        }
        return '#';
    }
}
