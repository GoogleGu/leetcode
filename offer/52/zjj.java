/**
 * 这个题看不懂不会做   觉得这样写挺好   虽然不知道为啥
 */

public class Solution {
    public boolean match(char[] str, char[] pattern)
    {
        return  new String(str).matches(new String(pattern));
    }
}