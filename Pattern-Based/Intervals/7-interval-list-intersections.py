def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    i = 0
    j = 0
    result = []

    while i < len(firstList) and j < len(secondList):
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1],secondList[j][1])

        if start <= end:
            result.append([start,end])

        if firstList[i][1] < secondList[j][1]:
            i = i + 1
        elif secondList[j][1] < firstList[i][1]:
            j = j + 1
        else:
            i = i + 1
            j = j + 1

    return result


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print(intervalIntersection(firstList,secondList))