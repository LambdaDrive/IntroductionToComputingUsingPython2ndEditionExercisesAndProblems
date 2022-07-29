def pascalLine(n):
    if n == 0:
        return [[1]]
    else:
        pascal = pascalLine(n-1)
        nowrow = [1]
        backrow = pascal[-1]
        for i in range(len(backrow)-1):
            nowrow.append(backrow[i] + backrow[i+1])
        nowrow += [1]
        pascal.append(nowrow)
        return pascal