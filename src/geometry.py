from dataclasses import dataclass, field
import numpy as np

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
        return np.sqrt(self.Vec.x ** 2 + self.Vec.y ** 2)
    def angle(self) -> float:
        return np.arctan2(self.Vec.y, self.Vec.x) % np.pi
    def center(self)->Point:
        return Point(self.A.x + self.B.x / 2, self.A.y + self.B.y / 2)