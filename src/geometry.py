from dataclasses import dataclass, field
import numpy as np

@dataclass
class Point:
    x: float
    y: float

    def __str__(self):
        return f"Point({self.x}, {self.y})"

@dataclass
class Line:
    A: Point
    B: Point
    Vec: Point = field(init=False)

    def __post_init__(self):
        self.Vec = Point(self.A.x - self.B.x, self.A.y - self.B.y)
    def __str__(self):
        return f"Line between ({self.A.x}, {self.A.y}) and ({self.B.x}, {self.B.y})"

    @property
    def length(self) -> float:
        return np.sqrt(self.Vec.x ** 2 + self.Vec.y ** 2)
    @property
    def angle(self) -> float:
        return np.arctan2(self.Vec.y, self.Vec.x) % np.pi
    @property
    def center(self)->Point:
        return Point(int((self.A.x + self.B.x) / 2), int((self.A.y + self.B.y) / 2))