PI = 3.14159


class Circle:
    def __init__(self, radius: float) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return PI * self.radius * self.radius

    def circumference(self) -> float:
        return 2 * PI * self.radius


class TrafficLight:
    def __init__(self) -> None:
        self.__color = "red"

    @property
    def color(self) -> str:
        return self.__color

    def running(self) -> None:
        for _ in range(3):
            if self.__color == "red":
                print("Color: red, duration: 7s")
                self.__color = "yellow"
            elif self.__color == "yellow":
                print("Color: yellow, duration: 2s")
                self.__color = "green"
            else:
                print("Color: green, duration: 5s")
                self.__color = "red"

    def switch(self, new_color: str) -> None:
        if self.__color == "red" and new_color != "yellow":
            raise RuntimeError("After red must be yellow")
        if self.__color == "yellow" and new_color != "green":
            raise RuntimeError("After yellow must be green")
        if self.__color == "green" and new_color != "red":
            raise RuntimeError("After green must be red")
        self.__color = new_color


def test_1() -> None:
    c1 = Circle(5)
    print("radius =", c1.radius)
    print("area =", round(c1.area(), 4))
    print("circumference =", round(c1.circumference(), 4))

    c2 = Circle(1)
    print("radius =", c2.radius)
    print("area =", round(c2.area(), 4))
    print("circumference =", round(c2.circumference(), 4))

    c3 = Circle(2.5)
    print("radius =", c3.radius)
    print("area =", round(c3.area(), 4))
    print("circumference =", round(c3.circumference(), 4))

    try:
        Circle(0)
    except ValueError as e:
        print("ValueError:", e)

    try:
        Circle(-3)
    except ValueError as e:
        print("ValueError:", e)

    try:
        Circle("abc")
    except TypeError as e:
        print("TypeError:", e)


def test_2() -> None:
    tl = TrafficLight()
    print("Initial color:", tl.color)

    tl.running()
    print("After running:", tl.color)

    try:
        tl.switch("red")
    except RuntimeError as e:
        print("RuntimeError:", e)

    tl.switch("yellow")
    print("Switched to:", tl.color)
    tl.switch("green")
    print("Switched to:", tl.color)
    tl.switch("red")
    print("Switched to:", tl.color)