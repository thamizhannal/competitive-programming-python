from typing import List
'''
Pair Sum - Sorted
Easy
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].

'''
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
if __name__ == '__main__':
    print("Hello ByteByteGo!")
    nums = [-5, -2, 3, 4, 6] 
    target = 7
    out = [2, 3]
    if pair_sum_sorted(nums=nums, target=target) == out:
        print("Paired Sum problem solved!")