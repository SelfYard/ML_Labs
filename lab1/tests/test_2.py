def fib_sum(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 0
    a, b = 0, 1
    total = a + b
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total


def test_1() -> None:
    n = int(input("Input fib index: "))
    print("Sum:", fib_sum(n))


def task_2(arg):
    if isinstance(arg, tuple):
        total = 0
        for item in arg:
            if isinstance(item, str):
                for word in item.split():
                    total += len(word)
        return total
    elif isinstance(arg, list):
        letters = 0
        numbers = 0
        for item in arg:
            if isinstance(item, str):
                letters += sum(ch.isalpha() for ch in item)
            elif isinstance(item, (int, float)):
                numbers += 1
        return letters, numbers
    elif isinstance(arg, (int, float)):
        return sum(
            int(ch) for ch in str(abs(arg))
            if ch.isdigit() and int(ch) % 2 == 1
        )
    elif isinstance(arg, str):
        return sum(ch.isalpha() for ch in arg)
    else:
        raise TypeError("Unsupported type")


def test_2() -> None:
    print(task_2(("asdasd", "asdsada")))
    print(task_2(("qwe asd", "aaa")))
    print(task_2(["a", "bc", 1, 2, "d"]))
    print(task_2(12345))
    print(task_2(-1234))
    print(task_2("Hello, World!"))

def check_and_invert(matrix):
    if all(any(x > 0 for x in row) for row in matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = -matrix[i][j]
    return matrix


def test_3() -> None:
    matrix1 = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9],
    ]
    print(check_and_invert(matrix1))

    matrix2 = [
        [-1, -2, -3],
        [4, -5, 6],
    ]
    print(check_and_invert(matrix2))


def divide(a, b):
    print("divide: start")
    try:
        print("try: dividing")
        result = a / b
        print(f"try: result = {result}")
        return result
    except ZeroDivisionError:
        print("except: division by zero")
        return None
    finally:
        print("finally: always executed")


def test_4() -> None:
    divide(10, 2)
    divide(10, 0)
    try:
        divide(10, "abc")
    except TypeError as e:
        print(f"outer except: caught {type(e).__name__}: {e}")