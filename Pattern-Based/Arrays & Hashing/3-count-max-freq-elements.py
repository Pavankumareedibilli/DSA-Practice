def maxFrequencyElements(self, nums: list[int]) -> int:
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_freq = 0
    for f in freq.values():
        max_freq = max(max_freq, f)

    ans = 0
    for f in freq.values():
        if f == max_freq:
            ans += f

    return ans


