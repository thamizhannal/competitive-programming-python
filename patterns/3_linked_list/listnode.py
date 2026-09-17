from __future__ import annotations
from typing import Optional
class LinkedNode:
    def __init__(self, val:int , next: Optional[LinkedNode] = None):
        self.val = val
        self.next = next

class DoubleLinkedNode:
    def __init__(self, val: int, prev:Optional[DoubleLinkedNode] = None, next: Optional[DoubleLinkedNode] = None):
        self.val = val
        self.prev = prev
        self.next = next

def linked_list_reverse(head: LinkedNode) -> LinkedNode:
        #To reverse a linked list, we can iterate through
        curr_node, prev_node = head, None
        print(f"curr_node:{curr_node.val}")
        while curr_node:
             next_node = curr_node.next
             curr_node.next = prev_node
             prev_node = curr_node
             curr_node = next_node
             print(f"prev_node:{prev_node.val}")
        return prev_node

def linked_list_reversal_recursive(head:LinkedNode) -> LinkedNode:

     if not head or not head.next:
          return head
     
     new_head = linked_list_reversal_recursive(head.next)

     head.next.next = head
     head.next = None 
     print(f"New head:{new_head.val} ")
     print(f"old head:{head.val}")
     return new_head

def remove_kth_last_node(head:LinkedNode, k: int) -> LinkedNode:
     # Path: 3_linked_list/listnode.py
     dummy = LinkedNode(-1)
     dummy.next = head
     leader = trailer = dummy

     for _ in range(k):
          leader = leader.next
          if not leader:
               return head

     while leader.next:
          leader = leader.next
          trailer = trailer.next
     trailer.next = trailer.next.next
     return dummy.next   
        
if __name__ == '__main__':
    # Creatin a simple Linked List 20->301->101
    node5 = LinkedNode(3,None)
    node4 = LinkedNode(7,node5)
    node3 = LinkedNode(4, node4)
    node2 = LinkedNode(2, node3)
    node1 = LinkedNode(1, node2)
    print("Linked Node!")

    
    print(f"Head Node:{node1.val}, next Node:{node2.val}, last Node:{node3.val}")
    remove_kth_last_node(node1,7)
    linked_list_reversal_recursive(node1)

    linked_list_reverse(node1)
    
    