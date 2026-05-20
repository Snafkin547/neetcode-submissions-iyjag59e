class CountSquares:

    def __init__(self):
        # keep track of coordinates of same x and y
        self.xy = defaultdict(list)
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        # add to both x and y map
        self.xy[point[0]].append(point[1])
        self.points[tuple(point)]+= 1
        

    def count(self, point: List[int]) -> int:
        # check vertical vs horizontal coordinates
        count = 0
        for y in self.xy[point[0]]:
            if y == point[1]:
                continue
            size = y - point[1]
            xpos, xneg = point[0] + size, point[0] - size
            count += self.points[(xpos, y)] * self.points[(xpos, point[1])]
            count += self.points[(xneg, y)] * self.points[(xneg, point[1])]
        return count
