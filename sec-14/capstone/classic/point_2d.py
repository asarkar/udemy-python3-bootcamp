from __future__ import annotations  # for Point2D forward references

import math
from functools import total_ordering


@total_ordering  # generate comparison methods
class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist(self, other: Point2D) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __eq__(self, other: Point2D) -> bool:
        return ((self.x, self.y) == (other.x, other.y))

    def __lt__(self, other: Point2D) -> bool:
        return ((self.x, self.y) < (other.x, other.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
