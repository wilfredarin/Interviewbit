class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        cur_idx = 1
        cur_node = A
        pre_seg =None
        seg_end = None
        seg_start = None
        while cur_idx <= C:
            if cur_idx ==B-1:
                pre_seg = cur_node
            if cur_idx == B:
                seg_start = cur_node
            if cur_idx == C:
                seg_end = cur_node
            cur_idx += 1
            cur_node = cur_node.next
        cur_node = seg_start.next
        seg_start.next = seg_end.next
        if B != 1:
            pre_seg.next = seg_end
        else:
            A = seg_end
        pre_node = seg_start
        Next = None
        while pre_node != seg_end:
            Next = cur_node.next
            cur_node.next=  pre_node
            pre_node= cur_node
            cur_node = Next
        return A
