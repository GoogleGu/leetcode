/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //获取长度
        int indexA = 0;
        int indexB = 0;
        ListNode headATemp = headA;
        ListNode headBTemp = headB;
        while(headATemp!=null||headBTemp!=null){
            if(headATemp==headBTemp){
                return headATemp;
            }
            if(headATemp!=null){
                headATemp = headATemp.next;
                indexA++;
            }
            if(headBTemp!=null){
                headBTemp = headBTemp.next;
                indexB++;
            }
        }
        if((indexA==0||indexB==0)&&indexA!=indexB){
            return null;
        }
        
        headATemp = headA;
        headBTemp = headB;

        if(indexA>indexB){
            return get(headATemp,headBTemp,indexA,indexB);
        }else{
            return get(headBTemp,headATemp,indexB,indexA);
        }
    }

    // 把长的缩减到和短的一样,再进行比较
    public ListNode get(ListNode chang,ListNode duan,int indexChang,int indexDuan){
        while(chang!=null&&indexChang>indexDuan){
            chang = chang.next;
            indexChang--;
        }
        while(chang!=null){
            if(chang==duan){
                return chang;
            }
            chang = chang.next;
            duan = duan.next;
        } 
        return null;
    }

}
