package com.yunlsp.pay.sdktest.controller;


import cn.hutool.core.thread.ThreadUtil;
import com.sun.org.apache.xpath.internal.WhitespaceStrippingElementMatcher;

import java.util.List;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
    ListNode(int x, ListNode next) {
        val = x;
        this.next = next;
    }
}

class Solution {

    public ListNode sortList(ListNode head) {
        //  0个节点 ||  1个节点
        if (head == null || head.next == null) {
            return head;
        }
        //  >= 2个节点
        ListNode first = head, second = null, mid = getMid(head);
        second = mid.next;
        mid.next = null;
        first = sortList(first);
        second = sortList(second);
        return merge(first, second);
    }

    // 排序
    ListNode merge(ListNode first, ListNode second) {
        if (first == null) {
            return second;
        }
        if (second == null) {
            return first;
        }

        ListNode res = new ListNode(0);
        //控制新链表顺序的point
        ListNode curr = res;

        while (first != null && second != null) {
            if (first.val < second.val) {
                curr.next = first;
                curr = curr.next;
                first = first.next;
            } else {
                curr.next = second;
                curr = curr.next;
                second = second.next;
            }
        }

        if (first != null) {
            curr.next = first;
        }
        if (second != null) {
            curr.next = second;
        }

        return res.next;
    }

    ListNode getMid(ListNode head) {
        ListNode slow = head, fast = head.next;

        while (fast!=null&&fast.next!=null) {
            slow=slow.next;
            fast=fast.next.next;
        }

        return slow;
    }


    public static void main(String[] args) {
        ListNode listNode = new ListNode(1, new ListNode(5, new ListNode(6, new ListNode(7, new ListNode(5, null)))));
        ListNode listNode1 = new Solution().sortList(listNode);
    }

}
