class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        return merge(l1,l2);
    }


    public ListNode merge(ListNode left,ListNode right){
        if(left==null&&right==null){
            return null;
        }
        ListNode temp = new ListNode(-1);
        ListNode curr = temp;
        while(left!=null && right!=null){
            if(left.val<=right.val){
                curr.next = left;
                left = left.next;
                curr = curr.next;
            }else{
                curr.next = right;
                right = right.next;
                curr = curr.next;
            }
        }
        if(left!=null){
            curr.next = left;
        }
        if(right!=null){
            curr.next=right;
        }
        return temp.next;
    }
}
