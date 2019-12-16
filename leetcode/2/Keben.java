class Solution {
    public ListNode addTwoNumbers(ListNode left, ListNode right) {
        ListNode sum = new ListNode(-1);
        ListNode curr = sum;
        int temp = 0;
        while(left != null || right!=null || temp != 0){
            if(left!=null){
                temp += left.val;
                left = left.next;
            }
            if(right!=null){
                temp += right.val;
                right = right.next;
            }
            int yu = temp % 10;
            temp = temp / 10;
            curr.next = new ListNode(yu);
            curr = curr.next;
        }
        return sum.next;
    }
}
