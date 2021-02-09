# from math import isclose


def classify_triangle(a: float, b: float, c: float) -> str:
    # [a, b, c] = sorted([a, b, c])
    if a + b <= c:  # Not Even a triangle
        return None
    if a == b == c:
        return "Equilateral Triangle"
    if a == b or b == c:
        if a * a + b * b == c * c:
            return "Right Isosceles Triangle"
        else:
            return "Isosceles Triangle"
    if a * a + b * b == c * c:
        return "Right Scalene Triangle"
    return "Scalene Triangle"
