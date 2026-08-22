from collections import Counter

def taskScheduler(tasks:list,n):
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = 0

    for value in freq.values():
        if value == max_freq:
            max_count = max_count + 1

    formule = (max_freq - 1)*(n+1) + max_count

    return max(len(tasks),formule)

tasks = ["A","A","A","B","B","B"]
print(taskScheduler(tasks,2))
