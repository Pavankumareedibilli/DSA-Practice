def employeeFreeTime(schedule:list[list[list]]) ->list[list]:
    intervals = []
    for employee in schedule:
        for start,end in employee:
            intervals.append([start,end])

    intervals.sort(key= lambda x:x[0])

    prev_end = intervals[0][1]

    free_time = []

    for start,end in intervals[1:]:
        if start > prev_end:
            free_time.append([prev_end,start])
            prev_end = end
        else:
            prev_end = max(prev_end,end)

    return free_time


