"""

Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example : 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
"""


def zigzagLevelOrder(self, A): 
        if A is None:
            return 
        curr_level = [A]
        next_level = []
        direction = True
        ans =[]
        output = []
        while curr_level:
            node = curr_level.pop()
            ans.append(node.val)
            if direction:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            if not curr_level:
                direction = not direction
                output.append(ans)
                ans = []
                curr_level = next_level
                next_level = []
        return output
