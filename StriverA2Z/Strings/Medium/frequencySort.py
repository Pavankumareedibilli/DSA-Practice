def frequencySort(s:str)->str:
    freq ={}
    result =[]
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    
    shorted_items = sorted(freq.items(), key=lambda item:item[1], reverse = True)

    for ch,count in shorted_items:
        result.append(ch*count)
    
    return "".join(result)

s="Three"
print(frequencySort(s))
