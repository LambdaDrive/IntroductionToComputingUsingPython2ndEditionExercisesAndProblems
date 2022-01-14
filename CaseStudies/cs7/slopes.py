def slopes(points):
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        slope = (y2 - y1) / (x2 - x1)
