from collections import defaultdict
def subarrsumeqk(arr ,k):
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    for num in arr:
        prefix_sum = prefix_sum+num
        if (prefix_sum-k) in freq:
            count = count + freq[prefix_sum-k]
        freq[prefix_sum] = freq[prefix_sum] +1
    return count
