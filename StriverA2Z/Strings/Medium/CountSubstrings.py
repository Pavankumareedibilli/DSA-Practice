def at_most_k_distinct(s:str,k):
    left = 0
    ans = 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1

        while len(freq)>k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left = left+1

        ans = ans + (right - left + 1)

    return ans

def countSubstrings(s,k):
    return at_most_k_distinct(s,k) - at_most_k_distinct(s,k-1)


s = "pqpqs"

print(countSubstrings(s,2))