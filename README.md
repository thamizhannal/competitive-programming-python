# Competitive Programming – Python

My playground for practicing competitive programming using Python

## Goals

- Refresh and improve problem-solving skills
- Experiment with common competitive programming patterns
- Review and master data structures and algorithms

## Repository Structure

```
algorithms/         → Algorithms and implementations
data_structures/    → Data structure implementations
patterns/           → Common problem-solving patterns
problems/           → Solutions to programming problems
```

### Patterns

#### 4_Fast_Slow_Pointer_Approach

**Happy Number Detection**  
The `happy_number.py` script implements a function to determine whether a given number is a "happy number." A happy number is a number that eventually reaches 1 when replaced by the sum of the square of each digit. If it loops endlessly in a cycle that does not include 1, then it is not a happy number.

**Implementation Approach:**

- **Fast and Slow Pointers (Floyd's Cycle-Finding Algorithm):**
  - The algorithm uses two pointers, slow and fast, both starting at the initial number.
  - The slow pointer moves one step at a, while the fast pointer moves two steps at a time.
  - If the number is a happy number, the fast pointer will eventually reach 1.
  - If a cycle is detected (i.e., fast and slow meet at the same node), the number is not a happy number.

- **Helper Function `get_next_num`:**
  - This function calculates the next number in the sequence by summing the squares of the digits of the current number.
  - It prints the intermediate steps for debugging purposes.
  - Example: For the input 43, the function will calculate the next numbers until it either reaches 1 (happy number) or detects a cycle (not a happy number).

**Linked List Loop Detection and Midpoint Finding**  
The `linked_list_loop_mid_point.py` script implements functions to detect a loop in a linked list and to find the midpoint of a linked list using the fast and slow pointers technique.

**Implementation Approach:**

- **Detecting a Loop in a Linked List:**
  - The `linked_list_loop` function uses two pointers, slow and fast, both starting at the head of the list.
  - The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
  - If a loop exists, the fast and slow pointers will eventually meet at the same node.
  - If they meet, a loop is detected.

- **Finding the Midpoint of a Linked List:**
  - The `linked_list_mid_point` function also uses the fast and slow pointers technique.
  - The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
  - When the fast pointer reaches the end of the list, the slow pointer will be at the midpoint.

**Helper Functions:**
- `print_list`: Prints the values of the linked list nodes.
- `linked_list_loop_naive_approach`: A naive approach to detect a loop by using a set to track visited nodes.

**Example:**  
For a linked list with nodes 51 -> 41 -> 31 -> 21 -> 11, the `linked_list_mid_point` function will return the midpoint node, which is 31.

**Summary:**  
- Happy Number Detection: Uses Floyd's Cycle-Finding Algorithm to detect cycles and determine if a number is happy.
- Linked List Loop Detection and Midpoint Finding: Uses the fast and slow pointers technique to detect loops and find the midpoint efficiently.

---

### 5_Sliding_Window_Approach

**Anagram Substring Detection**  
The `substring_anagrams.py` file contains a function `substring_anagrams` that finds the number of substrings in a string `s` that are anagrams of a string `t`.

**Implementation Approach:**

- **Problem Understanding:**  
  We need to find the number of substrings in `s` that are anagrams of `t`. An anagram of `t` is a substring of `s` that contains all the characters of `t` in the same frequency.

- **Sliding Window Technique:**  
  Use a sliding window of length equal to the length of `t` to traverse through `s`.  
  Maintain a frequency count of characters in the current window and compare it with the frequency count of `t`.

- **Frequency Count:**  
  Use two arrays of size 26 (for each letter in the alphabet) to store the frequency counts of characters in the current window and in `t`.

- **Window Adjustment:**  
  Expand the window by moving the right pointer and adjust the window by moving the left pointer when the window size exceeds the length of `t`.

- **Comparison:**  
  When the window size matches the length of `t`, compare the frequency counts of the current window with that of `t`. If they match, it means the current window is an anagram of `t`.

**Code Implementation:**  
The code provided in the file already implements this approach. Here's a brief explanation of the key parts:

- **Initialization:**  
  `window_char_freq` and `substr_char_freq` are arrays to store the frequency counts of characters in the current window and in `t`, respectively.

- **Sliding Window:**  
  The right pointer expands the window by moving through `s`.  
  When the window size matches the length of `t`, the code checks if the current window is an anagram of `t` by comparing the frequency counts.  
  If the window is an anagram, increment the `total_match` counter.  
  Adjust the window by moving the left pointer and updating the frequency count.

- **Edge Cases:**  
  If the length of `t` is greater than the length of `s`, return 0 as there can be no valid substrings.

**Example:**  
For the input:  
`s = "caabab"`  
`t = "aba"`  
The function will find all substrings of `s` that are anagrams of `t` and return the count.

**Efficiency:**  
This approach efficiently finds all anagram substrings in linear time, making it suitable for large input sizes.
Detecting a Loop in a Linked List:

The linked_list_loop  function uses two pointers, slow and fast, both starting at the head of the list.
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
If a loop exists, the fast and slow pointers will eventually meet at the same node.
If they meet, a loop is detected.
Finding the Midpoint of a Linked List:

The linked_list_mid_point  function also uses the fast and slow pointers technique.
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
When the fast pointer reaches the end of the list, the slow pointer will be at the midpoint.
Helper Functions:

print_list : Prints the values of the linked list nodes.
linked_list_loop_naive_approach : A naive approach to detect a loop by using a set to track visited nodes.
Example: For a linked list with nodes 51 -> 41 -> 31 -> 21 -> 11, the 
linked_list_mid_point
 function will return the midpoint node, which is 31.

**Summary**
Happy Number Detection: Uses Floyd's Cycle-Finding Algorithm to detect cycles and determine if a number is happy.
Linked List Loop Detection and Midpoint Finding: Uses the fast and slow pointers technique to detect loops and find the midpoint efficiently.


### 5_Sliding_Window_Approach
substring_anagrams.py
 file contains a function 
substring_anagrams
 that finds the number of substrings in a string s that are anagrams of a string t. Here's an implementation approach for the function:

**Approach Problem Understanding:**

We need to find the number of substrings in s that are anagrams of t.
An anagram of t is a substring of s that contains all the characters of t in the same frequency.
**Sliding Window Technique:**

Use a sliding window of length equal to the length of t to traverse through s.
Maintain a frequency count of characters in the current window and compare it with the frequency count of t.
**Frequency Count:**

Use two arrays of size 26 (for each letter in the alphabet) to store the frequency counts of characters in the current window and in t.
**Window Adjustment:**

Expand the window by moving the right pointer and adjust the window by moving the left pointer when the window size exceeds the length of t.
# Competitive Programming – Python

My playground for practicing competitive programming using Python

## Goals

- Refresh and improve problem-solving skills
- Experiment with common competitive programming patterns
- Review and master data structures and algorithms

## Repository Structure

```
algorithms/         → Algorithms and implementations
data_structures/    → Data structure implementations
patterns/           → Common problem-solving patterns
problems/           → Solutions to programming problems
```

### Patterns

#### 4_Fast_Slow_Pointer_Approach

**Happy Number Detection**  
The `happy_number.py` script implements a function to determine whether a given number is a "happy number." A happy number is a number that eventually reaches 1 when replaced by the sum of the square of each digit. If it loops endlessly in a cycle that does not include 1, then it is not a happy number.

**Implementation Approach:**

- **Fast and Slow Pointers (Floyd's Cycle-Finding Algorithm):**
  - The algorithm uses two pointers, slow and fast, both starting at the initial number.
  - The slow pointer moves one step at a, while the fast pointer moves two steps at a time.
  - If the number is a happy number, the fast pointer will eventually reach 1.
  - If a cycle is detected (i.e., fast and slow meet at the same node), the number is not a happy number.

- **Helper Function `get_next_num`:**
  - This function calculates the next number in the sequence by summing the squares of the digits of the current number.
  - It prints the intermediate steps for debugging purposes.
  - Example: For the input 43, the function will calculate the next numbers until it either reaches 1 (happy number) or detects a cycle (not a happy number).

**Linked List Loop Detection and Midpoint Finding**  
The `linked_list_loop_mid_point.py` script implements functions to detect a loop in a linked list and to find the midpoint of a linked list using the fast and slow pointers technique.

**Implementation Approach:**

- **Detecting a Loop in a Linked List:**
  - The `linked_list_loop` function uses two pointers, slow and fast, both starting at the head of the list.
  - The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
  - If a loop exists, the fast and slow pointers will eventually meet at the same node.
  - If they meet, a loop is detected.

- **Finding the Midpoint of a Linked List:**
  - The `linked_list_mid_point` function also uses the fast and slow pointers technique.
  - The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
  - When the fast pointer reaches the end of the list, the slow pointer will be at the midpoint.

**Helper Functions:**
- `print_list`: Prints the values of the linked list nodes.
- `linked_list_loop_naive_approach`: A naive approach to detect a loop by using a set to track visited nodes.

**Example:**  
For a linked list with nodes 51 -> 41 -> 31 -> 21 -> 11, the `linked_list_mid_point` function will return the midpoint node, which is 31.

**Summary:**  
- Happy Number Detection: Uses Floyd's Cycle-Finding Algorithm to detect cycles and determine if a number is happy.
- Linked List Loop Detection and Midpoint Finding: Uses the fast and slow pointers technique to detect loops and find the midpoint efficiently.

---

### 5_Sliding_Window_Approach

**Anagram Substring Detection**  
The `substring_anagrams.py` file contains a function `substring_anagrams` that finds the number of substrings in a string `s` that are anagrams of a string `t`.

**Implementation Approach:**

- **Problem Understanding:**  
  We need to find the number of substrings in `s` that are anagrams of `t`. An anagram of `t` is a substring of `s` that contains all the characters of `t` in the same frequency.

- **Sliding Window Technique:**  
  Use a sliding window of length equal to the length of `t` to traverse through `s`.  
  Maintain a frequency count of characters in the current window and compare it with the frequency count of `t`.

- **Frequency Count:**  
  Use two arrays of size 26 (for each letter in the alphabet) to store the frequency counts of characters in the current window and in `t`.

- **Window Adjustment:**  
  Expand the window by moving the right pointer and adjust the window by moving the left pointer when the window size exceeds the length of `t`.

- **Comparison:**  
  When the window size matches the length of `t`, compare the frequency counts of the current window with that of `t`. If they match, it means the current window is an anagram of `t`.

**Code Implementation:**  
The code provided in the file already implements this approach. Here's a brief explanation of the key parts:

- **Initialization:**  
  `window_char_freq` and `substr_char_freq` are arrays to store the frequency counts of characters in the current window and in `t`, respectively.

- **Sliding Window:**  
  The right pointer expands the window by moving through `s`.  
  When the window size matches the length of `t`, the code checks if the current window is an anagram of `t` by comparing the frequency counts.  
  If the window is an anagram, increment the `total_match` counter.  
  Adjust the window by moving the left pointer and updating the frequency count.

- **Edge Cases:**  
  If the length of `t` is greater than the length of `s`, return 0 as there can be no valid substrings.

**Example:**  
For the input:  
`s = "caabab"`  
`t = "aba"`  
The function will find all substrings of `s` that are anagrams of `t` and return the count.

**Efficiency:**  
This approach efficiently finds all anagram substrings in linear time, making it suitable for large input sizes.

When the window size matches the length of t, compare the frequency counts of the current window with that of t. If they match, it means the current window is an anagram of t.
Code Implementation
The code provided in the file already implements this approach. Here's a brief explanation of the key parts:

**Initialization**:

window_char_freq and substr_char_freq are arrays to store the frequency counts of characters in the current window and in t, respectively.
Sliding Window:

The right pointer expands the window by moving through s.
When the window size matches the length of t, the code checks if the current window is an anagram of t by comparing the frequency counts.
If the window is an anagram, increment the total_match counter.
Adjust the window by moving the left pointer and updating the frequency count.
Edge Cases:

If the length of t is greater than the length of s, return 0 as there can be no valid substrings.
**Example**
For the input:

s = "caabab"
t = "aba"
The function will find all substrings of s that are anagrams of t and return the count.

This approach efficiently finds all anagram substrings in linear time, making it suitable for large input sizes.
