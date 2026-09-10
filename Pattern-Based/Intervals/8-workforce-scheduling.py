def workforceScheduling(teamA,teamB,D):
    i = 0
    j = 0 
    result = []

    while i<len(teamA) and j < len(teamB):

        start = max(teamA[i][0],teamB[j][0])
        end = min(teamA[i][1],teamB[j][1])

        if start <= end:
            if end - start >= D:
                if len(result) < 3:
                    result.append([start,end])

        if teamA[i][1]<=teamB[j][1]:
            i = i + 1
        else:
            j = j + 1

    return result 


team_a = [[1, 5], [10, 20], [25, 30]]

team_b = [[2, 7], [12, 15], [18, 28]]

D = 3

print(workforceScheduling(team_a,team_b,D))
