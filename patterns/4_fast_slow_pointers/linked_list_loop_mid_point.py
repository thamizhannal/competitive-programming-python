
from __future__ import annotations
from typing import Optional


class LinkedNode:
    def __init__(self, val:int, next: Optional[LinkedNode] = None):
        self.value = val
        self.next = next
        
def linked_list_loop_naive_approach(head: LinkedNode) -> bool:
    seen_nodes = set()
    curr = head
    while curr:
        print(f"curr node:{curr.value} and curr next:{curr.next}")
        # cycle detection if the current node has already seen
        if curr in seen_nodes:
            return True
        seen_nodes.add(curr)
        curr = curr.next
    return False

def linked_list_loop(head:LinkedNode) -> bool :
    slow = fast  = head
    # check for both fast and fast->next pointers are present to avoid null condition
    while fast and fast.next:
        print(f"slow:{slow.value}, fast:{fast.value}")
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            print("Loop Found at node {curr.value}")
            return True
    return False

def print_list(head:LinkedNode) -> None:
    curr = head
    while curr:
        print(f"curr:{curr.value}->")
        curr = curr.next


def linked_list_mid_point(head:LinkedNode) -> int:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(f"Mid point of the list :{slow.value}")
    return slow



if __name__ == '__main__':
    print ("Hello world!")

    node4 = LinkedNode(101,None);
    node6 = LinkedNode(61, next=node4)
    print(f"{node6.value}, {node6.next}") 

    node1 = LinkedNode(11, next=node6)
    print(f"{node1.value} , {node1.next}")
    node2 = LinkedNode(21, next=node1)
    print(f"{node2.value}, {node2.next}") 
    node3 = LinkedNode(31, next=node2)
    print(f"{node3.value}, {node3.next}")
    node4 = LinkedNode(41, next=node3)
    print(f"{node4.value}, {node4.next}") 
    node5 = LinkedNode(51, next=node4)
    print(f"{node5.value}, {node5.next}") 

    print_list(node5)


    linked_list_loop_naive_approach(head=node5)

    linked_list_loop(head = node5)

    linked_list_mid_point(node5)
    node1.next = None
    linked_list_mid_point(node5)
     

    