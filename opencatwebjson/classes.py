from literals import Number
import math

class HexColor:
    def __init__(self, hex_code: str):
        if not (hex_code.startswith("#") and len(hex_code) in (4, 7)):
            raise ValueError("Invalid hex color")
        self.hex = hex_code.upper()

    def __str__(self):
        return self.hex

class Range01:
    def __init__(self, value: float):
        if not 0 <= value <= 1:
            raise ValueError("Value must be between 0 and 1")
        self.value = value

    def __float__(self):
        return self.value

    def __repr__(self):
        return f"Range01({self.value})"

class ScaleOffset:
    def __init__(self, scale: Number, offset: Number):
        if not 0 <= scale <= 1:
            raise ValueError("Scale must be between 0 and 1")
        self.scale = scale
        self.offset = offset

    def __repr__(self):
        return f"ScaleOffset(scale={self.scale}, offset={self.offset})"

class Vector2:
    def __init__(self, x: ScaleOffset, y: ScaleOffset):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

    def to_pixels(self, parent_width: Number, parent_height: Number) -> tuple[Number, Number]:
        """Converts scale+offset to absolute pixel coordinates."""
        px = self.x.scale * parent_width + self.x.offset
        py = self.y.scale * parent_height + self.y.offset
        return px, py

class Size2:
    def __init__(self, width: ScaleOffset, height: ScaleOffset):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Size2(width={self.width}, height={self.height})"

    def to_pixels(self, parent_width: Number, parent_height: Number) -> tuple[Number, Number]:
        """Convert scale+offset to absolute size in pixels."""
        w = self.width.scale * parent_width + self.width.offset
        h = self.height.scale * parent_height + self.height.offset
        return w, h

class Rotation:
    def __init__(self, degrees: Number):
        self.degrees = float(degrees)

    def __repr__(self):
        return f"Rotation({self.degrees}°)"

    def set(self, degrees: Number):
        self.degrees = float(degrees)

    def add(self, delta: Number):
        self.degrees += delta

    def normalized_360(self) -> float:
        """Return rotation in 0-360° range."""
        return self.degrees % 360

    def normalized_180(self) -> float:
        """Return rotation in -180° to 180° range."""
        deg = self.degrees % 360
        if deg > 180:
            deg -= 360
        return deg

    def to_radians(self) -> float:
        return math.radians(self.degrees)

class GradientStop:
    def __init__(self, position: float, value):
        if not 0 <= position <= 1:
            raise ValueError("Position must be between 0 and 1")
        self.position = position
        self.value = value

    def __repr__(self):
        return f"GradientStop(position={self.position}, value={self.value})"

class TransparencyGradient:
    def __init__(self, stops: List[GradientStop]):
        for stop in stops:
            if not isinstance(stop.value, (float, int)):
                raise TypeError("TransparencyGradient values must be float or int")
        self.stops = sorted(stops, key=lambda s: s.position)

    def __repr__(self):
        return f"TransparencyGradient({self.stops})"

    def get_value_at(self, position: float) -> float:
        if not 0 <= position <= 1:
            raise ValueError("Position must be between 0 and 1")
        # Simple linear interpolation between stops
        if position <= self.stops[0].position:
            return self.stops[0].value
        if position >= self.stops[-1].position:
            return self.stops[-1].value
        for i in range(len(self.stops)-1):
            s0, s1 = self.stops[i], self.stops[i+1]
            if s0.position <= position <= s1.position:
                t = (position - s0.position) / (s1.position - s0.position)
                return s0.value + t * (s1.value - s0.value)

class ColorGradient:
    def __init__(self, stops: List[GradientStop]):
        for stop in stops:
            if not isinstance(stop.value, str):
                raise TypeError("ColorGradient values must be hex strings")
        self.stops = sorted(stops, key=lambda s: s.position)

    def __repr__(self):
        return f"ColorGradient({self.stops})"

    def get_value_at(self, position: float) -> str:
        if not 0 <= position <= 1:
            raise ValueError("Position must be between 0 and 1")
        # Return nearest lower stop (simple approach)
        for stop in reversed(self.stops):
            if position >= stop.position:
                return stop.value
        return self.stops[0].value
