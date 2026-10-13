import heapq
def topKFreqElements(nums,k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1

    min_heap = []

    for key,value in freq.items():
        heapq.heappush(min_heap,(value,key))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = []

    for value,key in min_heap:
        result.append(key)

    return result

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFreqElements(nums,k))