"""
topology.py

The definitions of the topologies available by default for the world in Conway's Game of Life.
Other topologies can be created by implementing the normalize method.

:author: ℤ <sraaphorst@gmail.com>
"""

from enum import Enum, auto
from typing import Callable
from common import Position, Shape


class Alignment(Enum):
    OPEN = auto()
    LINKED = auto()
    REVERSED = auto()


# A Topology takes a Position and normalizes it according to the nature of the topology.
type Topology = Callable[[Position, Shape], Position | None]


def topology(
        row_alignment: Alignment,
        col_alignment: Alignment,
) -> Topology:
    """
    Create a topology with the specified row alignment and column alignment.

    row_alignment determines what happens when the row coordinate crosses its bounds:

        row = -1
         ↓
     ┌─────────────┐
     │             │
     │             │
     │             │
     └─────────────┘
         ↑
     row = nrows

    col_alignment determines what happens when the column coordinate crosses its bounds:

             ┌─────────────┐
    col=-1 → │             │ ← col=ncols
             │             │
             └─────────────┘
    """
    ...


torus = topology(
    row_alignment=Alignment.LINKED,
    col_alignment=Alignment.LINKED,
)

