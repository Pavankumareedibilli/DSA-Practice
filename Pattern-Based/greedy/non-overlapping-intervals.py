def nonOverlappingIntervals(intervals:list[list])->int:
    intervals.sort(key=lambda x : x[1])

    removed = 0
    curr_end = float("-inf")

    for start,end in intervals:
        if start >= curr_end:
            curr_end = end
        else:
            removed = removed + 1
    return removed

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(nonOverlappingIntervals(intervals))