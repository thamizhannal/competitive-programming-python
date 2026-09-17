class Node:
    """Represents a single node in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

def find_cycle_start(head):
    """
    Detects a cycle and returns the starting node of the loop.
    Returns None if no cycle exists.
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head
    print(f"Node={head.value}")
    # Step 1: Detect if a cycle exists
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        print(f"slow={slow.value}, fast={fast.value}")
        # If they meet, a cycle is confirmed
        if slow == fast:
            print(f"Circile is confirned at Node value {head.value}")
            break
    else:
        # If the loop finishes naturally, there is no cycle
        return None

    # Step 2: Find the entry point of the cycle
    # Reset slow pointer to the head of the list
    slow = head
    
    # Move both pointers at the same speed (1 step each)
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Both pointers meet at the starting node of the cycle
    return slow

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Create nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)

    # 2. Link nodes together: 10 -> 20 -> 30 -> 40
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # 3. Corrupt the list by making 40 point back to 20 (creating a cycle)
    node4.next = node2 

    # 4. Find the cycle
    corrupted_node = find_cycle_start(node1)

    if corrupted_node:
        print(f"Cycle detected! The corruption starts at node with value: {corrupted_node.value}")
    else:
        print("No cycle detected in the linked list.")
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    '''
    # Naive approach
    n = len(nums)
    for r in range(n):
        for c in range(r+1,n):
            if nums[r]+nums[c] == target:
                return [r,c] 
    return []

    Brute Force (Nested Loop): 
    Space complexity: O(N^2)
    Time complexity: O
    '''
    # approach2:
    # a + b = target
    # b = target -a 
    # -5 + b = 7 => b = 7-(-5) = 12
    # b = 12
    
    pair_sum_dict = {}
    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in pair_sum_dict :
            return [pair_sum_dict[complement], index]
        pair_sum_dict[nums[index]] = index
    return []
    '''
    Time complexity: O(N)
    Space complexity: O(N)
    '''
    '''
    Approch3: Use two pointer approach
    This replaces hashMap for holding entire array in memory
    Space complexity: O(1)
    Time: O(N)
    '''
    