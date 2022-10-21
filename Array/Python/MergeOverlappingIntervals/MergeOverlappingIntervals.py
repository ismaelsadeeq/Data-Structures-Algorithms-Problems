def mergeOverlappingIntervals(intervals):
    intervals.sort()
    output = []

    for start, end in intervals:
        if not output or start > output[-1][1]:
            output.append([start, end])
        else:
            output[-1][1] = max(output[-1][1], end)
    
    return output