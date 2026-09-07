def insertInterval(intervals:list,newInterval:list):
    new_start = newInterval[0]
    new_end = newInterval[1]

    i = 0
    n = len(intervals)
    result = []

    while i<n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i = i + 1


    while i<n and intervals[i][0] <= new_end:
        new_start = min(new_start,intervals[i][0])
        new_end = max(new_end,intervals[i][1])
        i = i + 1

    result.append([new_start,new_end])

    while i<n and intervals[i][0] > new_end:
        result.append(intervals[i])
        i = i + 1

    return result

intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
new = [4,8]

print(insertInterval(intervals,new))



