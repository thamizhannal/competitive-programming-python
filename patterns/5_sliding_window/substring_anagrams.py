
# s = c a a b a b
# t = a b a
def substring_anagrams(s:str, t:str) -> int :
    len_s , len_t = len(s), len(t)
    left, right = 0, 0

    if len_t > len_s:
        return 0

    total_match = 0

    window_char_freq, substr_char_freq =[0]*26, [0]*26
    for c in t:
        substr_char_freq[ord(c) - ord('a')] += 1
    
    while right < len_s:

        window_char_freq[ord(s[right]) - ord('a')] += 1

        if right - left + 1 == len_t:
            if window_char_freq == substr_char_freq:
                total_match += 1
            window_char_freq[ord(s[left]) - ord('a')] -=1
            left+=1
        right += 1
    return total_match


if __name__ == '__main__' :
    print("Hellow Sliding Window!")
    s = "caabab"
    t = "aba"
    print(f"Origional String:{s}, anagram string:{t}")
    print(substring_anagrams(s,t) )

