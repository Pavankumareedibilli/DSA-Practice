def meetingRooms(intervals:list):
    intervals.sort(key = lambda x:x[0])

    prev_end = intervals[0][1]

    for start,end in intervals[1:]:
        if start < prev_end:
            return False
        else:
            prev_end = end

    return True

print(meetingRooms([[7,10], [2,4], [1,3]]))