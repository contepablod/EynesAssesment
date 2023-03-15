# pi can be imported from math, numpy, scypy, etc.

class Circle():
    """
    A class representing a circle.

    Attributes:
    - radius (float): the radius of the circle

    Methods:
    - area(): returns the area of the circle
    - perimeter(): returns the perimeter of the circle
    - __str__(): returns a friendly string representation of the circle
    - __repr__(): returns a machine string representation of the circle that can be used to recreate it
    - __mul__(n): returns a new Circle object with radius multiplied by n

    Example:
    >>> c1 = Circle(2)
    >>> c1.radius
    2
    >>> c1.area()
    12.56636
    >>> c1.perimeter()
    12.56636
    >>> str(c1)
    'Circle with radius 2'
    >>> repr(c1)
    'Circle(2)'
    >>> c2 = c1 * 3
    >>> c2.radius
    6
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle object with the given radius.

        If radius is not positive or non-zero, raise a ValueError.

        Example:
        >>> c1 = Circle(2)
        >>> c1.radius
        2
        >>> c2 = Circle(-2)
        Traceback (most recent call last):
            ...
        ValueError: Radius must be positive and non-zero
        """

        if radius <= 0:
            raise ValueError("Radius must be positive and non-zero")
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Example:
        >>> c1 = Circle(2)
        >>> c1.area()
        12.56636
        """

        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the circle.

        Example:
        >>> c1 = Circle(2)
        >>> c1.perimeter()
        12.56636
        """

        return 2 * 3.14159 * self.radius

    def __str__(self) -> str:
        """
        Return a human_readable string representation of the circle.

        Example:
        >>> c1 = Circle(2)
        >>> str(c1)
        'Circle with radius 2'
        """

        return f"Circle with radius {self.radius}"

    def __repr__(self) -> str:
        """
        Return a machine-developer string representation of the circle.

        Example:
        >>> c1 = Circle(2)
        >>> repr(c1)
        'Circle(2)'
        """

        return f"Circle({self.radius})"

    def __mul__(self, n: float) -> float:
        """
        Multiply the radius of the circle by a positive integer n and return a new Circle object.

        If n is not positive or non-zero, raise a ValueError.

        Example:
        >>> c1 = Circle(2)
        >>> c2 = c1 * 3
        >>> c2.radius
        6
        >>> c1 * -2
        Traceback (most recent call last):
            ...
        ValueError: Multiplier must be positive and non-zero
        """

        if n <= 0:
            raise ValueError("Multiplier must be positive and non-zero")
        return Circle(self.radius * n)
