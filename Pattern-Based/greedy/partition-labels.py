def partitionLabels(s:str)->list[int]:
    last = {}
    for i,char in enumerate(s):
        last[char] = i
    end = 0
    start = 0
    result = []
    for i,char in enumerate(s):
        end = max(end,last[char])
        if i == end:
            result.append(i - start + 1)
            start = i+1
    return result

s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))

