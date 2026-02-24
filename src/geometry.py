from dataclasses import dataclass, field
from numpy import sqrt as sqrt

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Line:
    A: Point
    B: Point
    Vec: Point = field(init=False)

    def __post_init__(self):
        self.Vec = Point(self.A.x - self.B.x, self.A.y - self.B.y)

    def length(self) -> float:
        return sqrt(self.Vec.x ** 2 + self.Vec.y ** 2)