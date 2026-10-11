def is_anagaram(s:str,t:str):

    freq = {}

    if len(s) != len(t):
        return False

    for ch in s:
        freq[ch] = freq.get(ch,0) + 1

    for ch in t:
        freq[ch] = freq.get(ch,0) - 1

    for count in freq.values():
        if count!=0:
            return False

    return True
