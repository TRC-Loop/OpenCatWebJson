# Compatibility Notice:
# CatWeb v2.13.0.7 (Mega Update P2)

from dataclasses import dataclass
from typing import Any
from literals import CanvasSize, FontStyle, FontWeight, HorizontalAlignment, ListDirection, MaxSize, OutlineMode, OutlineType, ProductType, ResampleMode, ScaleType, TextSize, Truncate, Tuple2, Vec2, VerticalAlignment
from classes import ColorGradient, HexColor, Range01, Rotation, Size2, TransparencyGradient, Vector2

@dataclass
class Page:
    background_color: HexColor
    page_title: str
    icon: int # Decal ID
    search_description: str
    thumbnail: int # Decal ID

@dataclass
class Frame:
    name: str
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool

@dataclass
class Text:
    name: str
    text: str
    font: str
    font_style: FontStyle
    font_weight: FontWeight
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    text_size: TextSize
    text_color: HexColor
    text_transparency: Range01
    rich: bool
    wrap: bool
    truncate: Truncate
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool


@dataclass
class Image:
    name: str
    image_id: int # Decal ID
    image_transparency: Range01
    scale_type: ScaleType
    tint: HexColor
    resample_mode: ResampleMode
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool


@dataclass
class Link:
    name: str
    reference: str
    open_in_new_tab: bool
    text: str
    font: str
    font_style: FontStyle
    font_weight: FontWeight
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    text_size: TextSize
    text_color: HexColor
    text_transparency: Range01
    automatic_color: bool
    rich: bool
    wrap: bool
    truncate: Truncate
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool

@dataclass
class Button:
    name: str
    text: str
    font: str
    font_style: FontStyle
    font_weight: FontWeight
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    text_size: TextSize
    text_color: HexColor
    text_transparency: Range01
    automatic_color: bool
    rich: bool
    wrap: bool
    truncate: Truncate
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool

@dataclass
class Donation:
    name: str
    item_id: int
    reference: str
    product_type: ProductType    
    text: str
    font: str
    font_style: FontStyle
    font_weight: FontWeight
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    text_size: TextSize
    text_color: HexColor
    text_transparency: Range01
    automatic_color: bool
    rich: bool
    wrap: bool
    truncate: Truncate
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool


@dataclass
class Input:
    name: str
    placeholder: str
    text: str
    font: str
    font_style: FontStyle
    font_weight: FontWeight
    horizontal_alignment: HorizontalAlignment
    vertical_alignment: VerticalAlignment
    text_size: TextSize
    text_color: HexColor
    text_transparency: Range01
    placeholder_color: HexColor
    automatic_color: bool
    rich: bool
    wrap: bool
    truncate: Truncate
    editable: bool
    multi_line: bool
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool

@dataclass
class ScrollableFrame:
    name: str
    scrollbar_color: HexColor
    scrollbar_transparency: Range01
    scrollbar_thickness: int
    canvas_size: CanvasSize 
    background_transparency: Range01
    background_color: HexColor
    position: Vector2 
    size: Size2
    rotation: Rotation
    anchor_point: Vec2
    layer: int
    tooltip: str
    clip_descendants: bool
    visible: bool

@dataclass
class Script:
    name: str
    enabled: bool
    _content: Any # TODO: Implement Scripts/_content

# Styling Elements

@dataclass
class Outline:
    name: str
    mode: OutlineMode
    type: OutlineType
    outline_color: HexColor
    outline_thickness: int
    outline_transparency: Range01

@dataclass
class Corner:
    name: str
    radius: Tuple2 

@dataclass
class List:
    name: str
    direction: ListDirection
    padding: Tuple2 
    vertical_alignment: VerticalAlignment
    horizontal_alignment: HorizontalAlignment
    wrap: bool

@dataclass
class Grid:
    name: str
    padding: Tuple2
    size: Size2
    vertical_alignment: VerticalAlignment
    horizontal_alignment: HorizontalAlignment

@dataclass
class AspectRatio:
    name: str
    ratio: int

@dataclass
class Constraint:
    name: str
    minimum_size: Tuple2
    maximum_size: MaxSize

@dataclass
class Gradient:
    name: str
    rotation: Rotation
    offset: Tuple2
    gradient_transparency: TransparencyGradient
    gradient_color: ColorGradient

@dataclass
class Padding:
    name: str
    bottom: Tuple2
    left: Tuple2
    right: Tuple2
    top: Tuple2
