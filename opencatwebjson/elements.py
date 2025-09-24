# Compatibility Notice:
# CatWeb v2.13.0.7 (Mega Update P2)

from dataclasses import dataclass
from typing import Any
from .literals import CanvasSize, FontStyle, FontWeight, HorizontalAlignment, ListDirection, MaxSize, OutlineMode, OutlineType, ProductType, ResampleMode, ScaleType, TextSize, Truncate, Tuple2, Vec2, VerticalAlignment
from .classes import ColorGradient, HexColor, Range01, Rotation, Size2, TransparencyGradient, Vector2

@dataclass
class Page:
    """
    Represents a page in the application with visual and metadata properties.
    
    Attributes:
        background_color (HexColor): Page background color.
        page_title (str): Title of the page.
        icon (int): ID of the page icon decal.
        search_description (str): Description for search functionality.
        thumbnail (int): ID of the page thumbnail decal.
    """
    background_color: HexColor
    page_title: str
    icon: int
    search_description: str
    thumbnail: int

@dataclass
class Frame:
    """
    A container UI element for grouping and positioning child elements.
    
    Attributes:
        name (str): Frame identifier.
        background_transparency (Range01): Background transparency (0-1).
        background_color (HexColor): Background color of the frame.
        position (Vector2): Position of the frame.
        size (Size2): Width and height of the frame.
        rotation (Rotation): Rotation applied to the frame.
        anchor_point (Vec2): Anchor point for positioning.
        layer (int): Rendering order index.
        tooltip (str): Tooltip text displayed on hover.
        clip_descendants (bool): If True, child elements outside bounds are clipped.
        visible (bool): Determines visibility of the frame.
    """
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
    """
    Represents a text UI element with styling and layout properties.
    
    Attributes:
        name (str): Element identifier.
        text (str): Displayed text.
        font (str): Font name.
        font_style (FontStyle): Font style (e.g., italic).
        font_weight (FontWeight): Font weight (e.g., bold).
        horizontal_alignment (HorizontalAlignment): Horizontal text alignment.
        vertical_alignment (VerticalAlignment): Vertical text alignment.
        text_size (TextSize): Text size.
        text_color (HexColor): Text color.
        text_transparency (Range01): Text transparency (0-1).
        rich (bool): Enables rich text formatting.
        wrap (bool): Text wraps inside bounds.
        truncate (Truncate): Truncation mode for overflowing text.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position of the text element.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied to text.
        anchor_point (Vec2): Anchor point for positioning.
        layer (int): Rendering layer index.
        tooltip (str): Tooltip text on hover.
        clip_descendants (bool): Clips children if True.
        visible (bool): Visibility of the element.
    """
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
    """
    Represents an image element in the UI.
    
    Attributes:
        name (str): Element identifier.
        image_id (int): ID of the decal image. See: [Roblox Decal Store](https://create.roblox.com/store/decals) 
        image_transparency (Range01): Image transparency.
        scale_type (ScaleType): Scaling mode of the image.
        tint (HexColor): Tint applied to the image.
        resample_mode (ResampleMode): Image resampling mode.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position of the image element.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point for positioning.
        layer (int): Rendering order index.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clips children if True.
        visible (bool): Visibility.
    """
    name: str
    image_id: int
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
    """
    Clickable hyperlink UI element with text styling.
    
    Attributes:
        name (str): Element identifier.
        reference (str): URL or internal reference target.
        open_in_new_tab (bool): Opens link in a new tab if True.
        text (str): Displayed text.
        font (str): Font name.
        font_style (FontStyle): Font style.
        font_weight (FontWeight): Font weight.
        horizontal_alignment (HorizontalAlignment): Horizontal text alignment.
        vertical_alignment (VerticalAlignment): Vertical text alignment.
        text_size (TextSize): Text size.
        text_color (HexColor): Text color.
        text_transparency (Range01): Text transparency.
        automatic_color (bool): Automatically adjust color based on theme.
        rich (bool): Enables rich text.
        wrap (bool): Enables text wrapping.
        truncate (Truncate): Text truncation method.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point.
        layer (int): Rendering order.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clips children if True.
        visible (bool): Visibility.
    """
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
    """
    Clickable button element with text and styling properties.
    
    Attributes:
        name (str): Element identifier.
        text (str): Displayed text.
        font (str): Font name.
        font_style (FontStyle): Font style.
        font_weight (FontWeight): Font weight.
        horizontal_alignment (HorizontalAlignment): Text horizontal alignment.
        vertical_alignment (VerticalAlignment): Text vertical alignment.
        text_size (TextSize): Text size.
        text_color (HexColor): Text color.
        text_transparency (Range01): Text transparency.
        automatic_color (bool): Adjust color automatically.
        rich (bool): Rich text enabled.
        wrap (bool): Wrap text inside element.
        truncate (Truncate): Truncation method.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point.
        layer (int): Rendering layer.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clip children.
        visible (bool): Visibility.
    """
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
    """
    Represents a purchasable donation item element.
    
    Attributes:
        name (str): Element identifier.
        item_id (int): ID of the item.
        reference (str): Reference URL or product link.
        product_type (ProductType): Type of product.
        text (str): Displayed text.
        font (str): Font name.
        font_style (FontStyle): Font style.
        font_weight (FontWeight): Font weight.
        horizontal_alignment (HorizontalAlignment): Text alignment horizontal.
        vertical_alignment (VerticalAlignment): Text alignment vertical.
        text_size (TextSize): Text size.
        text_color (HexColor): Text color.
        text_transparency (Range01): Text transparency.
        automatic_color (bool): Auto color adjustment.
        rich (bool): Enable rich text.
        wrap (bool): Wrap text.
        truncate (Truncate): Truncate method.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point.
        layer (int): Rendering order.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clip children if True.
        visible (bool): Visibility.
    """
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
    """
    Input text element for user input.
    
    Attributes:
        name (str): Element identifier.
        placeholder (str): Placeholder text.
        text (str): Current input text.
        font (str): Font name.
        font_style (FontStyle): Font style.
        font_weight (FontWeight): Font weight.
        horizontal_alignment (HorizontalAlignment): Text horizontal alignment.
        vertical_alignment (VerticalAlignment): Text vertical alignment.
        text_size (TextSize): Text size.
        text_color (HexColor): Text color.
        text_transparency (Range01): Text transparency.
        placeholder_color (HexColor): Placeholder text color.
        automatic_color (bool): Auto color adjustment.
        rich (bool): Rich text enabled.
        wrap (bool): Wrap text inside bounds.
        truncate (Truncate): Truncate method.
        editable (bool): If True, text is editable.
        multi_line (bool): Multi-line input.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point.
        layer (int): Rendering layer.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clip children if True.
        visible (bool): Visibility.
    """
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
    """
    Frame element with a scrollable canvas.
    
    Attributes:
        name (str): Element identifier.
        scrollbar_color (HexColor): Scrollbar color.
        scrollbar_transparency (Range01): Scrollbar transparency.
        scrollbar_thickness (int): Scrollbar thickness.
        canvas_size (CanvasSize): Scrollable canvas size.
        background_transparency (Range01): Background transparency.
        background_color (HexColor): Background color.
        position (Vector2): Position.
        size (Size2): Width and height.
        rotation (Rotation): Rotation applied.
        anchor_point (Vec2): Anchor point.
        layer (int): Rendering layer.
        tooltip (str): Tooltip text.
        clip_descendants (bool): Clip children if True.
        visible (bool): Visibility.
    """
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
    """
    Script element representing executable code.
    
    Attributes:
        name (str): Script identifier.
        enabled (bool): If True, the script is active.
        _content (Any): Script content placeholder (implementation TBD).
    """
    name: str
    enabled: bool
    _content: Any

@dataclass
class Outline:
    """
    Styling outline applied to UI elements.
    
    Attributes:
        name (str): Outline identifier.
        mode (OutlineMode): Outline mode.
        type (OutlineType): Outline type.
        outline_color (HexColor): Outline color.
        outline_thickness (int): Outline thickness.
        outline_transparency (Range01): Outline transparency.
    """
    name: str
    mode: OutlineMode
    type: OutlineType
    outline_color: HexColor
    outline_thickness: int
    outline_transparency: Range01

@dataclass
class Corner:
    """
    Rounded corner styling for UI elements.
    
    Attributes:
        name (str): Corner identifier.
        radius (Tuple2): Corner radius.
    """
    name: str
    radius: Tuple2

@dataclass
class List:
    """
    A list container layout element.
    
    Attributes:
        name (str): Element identifier.
        direction (ListDirection): List direction (vertical/horizontal).
        padding (Tuple2): Padding between items.
        vertical_alignment (VerticalAlignment): Vertical alignment of list items.
        horizontal_alignment (HorizontalAlignment): Horizontal alignment.
        wrap (bool): If True, items wrap within container.
    """
    name: str
    direction: ListDirection
    padding: Tuple2
    vertical_alignment: VerticalAlignment
    horizontal_alignment: HorizontalAlignment
    wrap: bool

@dataclass
class Grid:
    """
    Grid container layout element.
    
    Attributes:
        name (str): Element identifier.
        padding (Tuple2): Padding between grid cells.
        size (Size2): Cell size.
        vertical_alignment (VerticalAlignment): Vertical alignment.
        horizontal_alignment (HorizontalAlignment): Horizontal alignment.
    """
    name: str
    padding: Tuple2
    size: Size2
    vertical_alignment: VerticalAlignment
    horizontal_alignment: HorizontalAlignment

@dataclass
class AspectRatio:
    """
    Maintains a fixed aspect ratio for an element.
    
    Attributes:
        name (str): Element identifier.
        ratio (int): Width-to-height ratio.
    """
    name: str
    ratio: int

@dataclass
class Constraint:
    """
    Size constraints for UI elements.
    
    Attributes:
        name (str): Element identifier.
        minimum_size (Tuple2): Minimum width and height.
        maximum_size (MaxSize): Maximum allowed size.
    """
    name: str
    minimum_size: Tuple2
    maximum_size: MaxSize

@dataclass
class Gradient:
    """
    Gradient styling element.
    
    Attributes:
        name (str): Element identifier.
        rotation (Rotation): Gradient rotation.
        offset (Tuple2): Gradient offset.
        gradient_transparency (TransparencyGradient): Transparency gradient.
        gradient_color (ColorGradient): Color gradient.
    """
    name: str
    rotation: Rotation
    offset: Tuple2
    gradient_transparency: TransparencyGradient
    gradient_color: ColorGradient

@dataclass
class Padding:
    """
    Padding applied to a UI element.
    
    Attributes:
        name (str): Element identifier.
        bottom (Tuple2): Bottom padding.
        left (Tuple2): Left padding.
        right (Tuple2): Right padding.
        top (Tuple2): Top padding.
    """
    name: str
    bottom: Tuple2
    left: Tuple2
    right: Tuple2
    top: Tuple2
