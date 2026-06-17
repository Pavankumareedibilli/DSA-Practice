def longestsubarraywithsumeqk(nums,k):

    prefix_freq={}
    max_len = 0
    current_sum = 0

    for i in range(len(nums)):
        current_sum = current_sum+ nums[i]

        if current_sum ==k:
            max_len = i+1

        if (current_sum-k) in prefix_freq:
            len = i - prefix_freq[current_sum-k]
            max_len= max(max_len,len)
        if current_sum not in prefix_freq:
            prefix_freq[current_sum] = i 

    return max_len