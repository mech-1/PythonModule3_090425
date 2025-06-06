from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 70), Point(5, -2), Point(10, -16), Point(-12, 0)]

zero_point = Point(0, 0)

max_dist = 0
max_point = points[0]

for point in points:
    if point.dist_to(zero_point) > max_dist:
        max_dist = point.dist_to(zero_point)
        max_point = point

print(f"Координаты наиболее удаленной точки = x:{max_point.x} y:{max_point.y}")
