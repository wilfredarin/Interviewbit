def deleteDuplicates(self, A):
        i = A.val
        temp = A
        while temp.next:
            while temp.next and i == temp.next.val:
                temp.next = temp.next.next
                if not temp.next:
                    return A
            i = temp.next.val
            temp = temp.next
        return A
