
from typing import Literal, Union, NamedTuple
from .classes import Size2

Number = Union[int, float]

# Tuples
class Vec2(NamedTuple):
    """Represents a 2D vector with x and y coordinates."""
    x: float
    y: float

Tuple2 = tuple[Number, Number]
"""A 2-element tuple of numbers, typically used for size or position."""


# Literal type definitions
FontStyle = Literal["normal", "italic"]
"""Font style options for text elements."""

FontWeight = Literal[
    "thin", "extralight", "light", "regular", "medium",
    "semibold", "bold", "extrabold", "heavy"
]
"""Font weight options for text elements."""

HorizontalAlignment = Literal["center", "left", "right"]
"""Horizontal alignment options for text or UI elements."""

VerticalAlignment = Literal["bottom", "center", "top"]
"""Vertical alignment options for text or UI elements."""

Truncate = Literal["atend", "none", "splitword"]
"""Text truncation behavior when content overflows."""

ScaleType = Literal["crop", "fit", "slice", "stretch", "tile"]
"""How images or UI elements scale within a container."""

ResampleMode = Literal["default", "pixelated"]
"""Resampling mode for image scaling."""

ProductType = Literal["asset", "gamepass", "product"]
"""Type of product or item being referenced."""

OutlineMode = Literal["border", "contextual"]
"""Outline rendering mode for text. Contextual only works when rich markup is disabled."""

OutlineType = Literal["bevel", "miter", "round"]
"""Type of outline geometry for text elements."""

ListDirection = Literal["horizontal", "vertical"]
"""Direction for list layouts or container stacking."""


# Union type definitions
TextSize = Union[int, float, Literal["scaled"]]
"""Font size, which can be a number in pixels or 'scaled' for dynamic sizing."""

CanvasSize = Union[Size2, Literal["auto", "auto_x", "auto_y"]]
"""Canvas size, either an absolute Size2 or automatic sizing options."""

MaxSize = Union[Tuple2, Literal["inf"]]
"""Maximum size constraint, either a tuple of numbers or 'inf' for unlimited."""
