def binarysubarr(nums,k):
    prefix_freq = {0,1}
    current_sum = 0
    result = 0

    for num in nums:
        current_sum = current_sum + num

        if (current_sum-k) in prefix_freq:
            result = result + prefix_freq[current_sum-k]

        prefix_freq[current_sum] = prefix_freq.get(current_sum,0) +1

    return result