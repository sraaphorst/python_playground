"""
world.py

Defines the World in Conway's Game of Life.

:author: ℤ <sraaphorst@gmail.com>
"""

from dataclasses import dataclass

from common import Grid, Status


# The probabilities used in world initialization.
probabilities: frozendict[Status, float] = frozendict({
    Status.ON: 0.2,
    Status.OFF: 0.8,
})


@dataclass
class World:
    """
    The world's current state in Conway's Game of Life.
    This consists of a numpy array Z_{ny} x Z_{nx}, i.e. ny rows and nx columns.
    The world is taken to be toroidal.
    """
    grid: Grid
