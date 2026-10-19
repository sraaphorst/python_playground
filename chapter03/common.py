"""
common.py

Common code for the implementation of Conway's Game of Life.

:author: ℤ <sraaphorst@gmail.com>
"""

from enum import IntEnum
import numpy as np

# A Grid is a rectangular section of tiles along with their values.
type Grid = np.ndarray[
    tuple[int, int],
    np.dtype[np.uint8],
]


# A Position is a position on a grid, indexed first by row and then by column.
type Position = tuple[int, int]

# The Shape of a grid, used by functions like topologies to properly map Position types
# to valid ranges.
type Shape = tuple[int, int]


class Status(IntEnum):
    """
    The status of a pixel: either ON or OFF.
    """
    ON = 255
    OFF = 0
