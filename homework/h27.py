import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example Usage:
my_circle = Circle(radius=5)

print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.area():.2f}")

print(f"Perimeter: {my_circle.perimeter():.2f}")

another_circle = Circle(radius=12.5)
print(f"\nRadius: {another_circle.radius}")
print(f"Area: {another_circle.area():.2f}")
print(f"Perimeter: {another_circle.perimeter():.2f}")