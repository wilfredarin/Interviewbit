"""

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

Using recursion is not allowed.

"""

#Method 1 using 1 Stack
def postorderTraversal(self, A):
        stack = []
        res = []
        cur_node = A
        while cur_node or stack:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    res.append(temp.val)
                    while stack and temp==stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.val)
                else:
                    cur_node = temp
        return res
        
#Method 2
def postorderTraversal(self, A):
        result = [] 
        d = [A]
        while d:
            node = d.pop()
            if node:
                result.append(node.val)
                d.append(node.left)
                d.append(node.right)
        return result[::-1]
