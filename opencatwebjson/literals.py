from typing import Literal, Union, NamedTuple
from classes import Size2

Number = Union[int, float]

# Tuples
class Vec2(NamedTuple):
    x: float
    y: float

Tuple2 = tuple[Number, Number]

# Literals
FontStyle = Literal["normal", "italic"]
FontWeight = Literal["thin", "extralight", "light", "regular", "medium", "semibold", "bold", "extrabold", "heavy"]
HorizontalAlignment = Literal["center", "left", "right"]
VerticalAlignment = Literal["bottom", "center", "top"]
Truncate = Literal["atend", "none", "splitword"]
ScaleType = Literal["crop", "fit", "slice", "stretch", "tile"]
ResampleMode = Literal["default", "pixelated"]
ProductType = Literal["asset", "gamepass", "product"]
OutlineMode = Literal["border", "contextual"] # Contextual only works when text has rich markup disabled
OutlineType = Literal["bevel", "miter", "round"]
ListDirection = Literal["horizontal", "vertical"]

# Unions
TextSize = Union[int, float, Literal["scaled"]]
CanvasSize = Union[Size2, Literal["auto", "auto_x", "auto_y"]]
MaxSize = Union[Tuple2, Literal["inf"]]
