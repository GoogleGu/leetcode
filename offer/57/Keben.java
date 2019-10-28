// 中序遍历规则,
    先左,再根,后右

// 1.若该节点存在右子树：则下一个节点为右子树最左子节点
// 2.若当前节点不存在右子树
//  2.1 若当前节点是上一个节点的左节点,那么下一个节点就是当前节点的父节点
//  2.2 若当前节点是上一个节点的右节点,那么下一个节点肯定不是父节点,应该往上找
*/
public class Solution {
 public TreeLinkNode GetNext(TreeLinkNode pNode) {
        if(pNode == null) {return null;}
        if(pNode.right != null) {    //如果有右子树，则找右子树的最左节点
            pNode = pNode.right;
            while (pNode.left != null) {pNode = pNode.left;}
            return pNode;
        }
        while(pNode.next != null) { //没右子树，则找第一个父节点的左节点的子节点
            if(pNode.next.left == pNode){ return pNode.next;}
            pNode = pNode.next;
        }
        return null;   //退到了根节点仍没找到，则返回null
    }
}
