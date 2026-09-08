def campaignsFreeTime(campaigns:list[list[list]],cooldown:int,d:int)->list:

    intervals = []

    for camps in campaigns:
        for start,end in camps:
            intervals.append([start,end+cooldown])

    intervals.sort(key = lambda x:x[0])

    prev_end = intervals[0][1]

    free_time = []

    for start,end in intervals[1:]:

        if start > prev_end:
            if start - prev_end >= d:
                free_time.append([prev_end,start])

            prev_end = end
        else:

            prev_end = max(prev_end,end)

    return free_time


campaigns = [
    [[10,12], [15,16]],
    [[20,21]]
]

cooldown = 1
D = 2

print(campaignsFreeTime(campaigns,cooldown,D))