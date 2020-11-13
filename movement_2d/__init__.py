"""This package contains various functions pertaining to 2d movement."""

from math import atan2, cos, pi, sin
from typing import List, Tuple

__all__: List[str] = [
    'normalise_angle', 'angle2rad', 'coordinates_in_direction', 'angle_between'
]


def normalise_angle(angle: int) -> int:
    """Return an angle between 0 and 359 degrees. If it is more or less
    than that, it will wrap around."""
    if angle < 0:
        return angle + 360
    elif angle > 359:
        return angle - 360
    return angle


def angle2rad(angle: int) -> float:
    """Converts an angle to radians. Formula taken from
    https://synthizer.github.io/tutorials/python.html"""
    return (angle / 180.0) * pi


def coordinates_in_direction(
    start_x: float, start_y: float, angle: int, distance: float = 1.0
) -> Tuple[float, float]:
    """Returns the coordinates that lie distance in direction from (start_x,
    start_y)."""
    rad: float = angle2rad(angle)
    x: float = start_x + (distance * sin(rad))
    y: float = start_y + (distance * cos(rad))
    return x, y


def angle_between(
    x1: float, y1: float,
    x2: float, y2: float
) -> float:
    """Returns the angle between two points.

    For example::
        angle_between(0, 0, 1, 1) == 45

    Code provided by Walter Plinge.
    """
    angle: float
    # Check if the points are on top of each other and output something reasonable.
    if x1 == x2 and y1 == y2:
        return 0
    # If y1 and y2 are the same, we'll end up dividing by 0, and that's bad.
    if y1 == y2:
        if x2 > x1:
            return 90
        else:
            return 270
    angle = atan2(x2 - x1, y2 - y1)
    # Convert result from radians to degrees. If you want minutes and seconds as well it's tough.
    angle = angle * 180 / pi
    # Ensure the angle is between 0 and 360.
    angle = normalise_angle(angle)
    return angle
