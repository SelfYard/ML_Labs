def test_1() -> None:
    n = int(input("Enter an integer: "))
    n = abs(n)

    if n == 0:
        print("0 has infinitely many divisors.")
        return

    print("Divisors:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def test_2() -> None:
    text = input("Enter a string: ")
    words = text.split()

    if len(words) == 0:
        print("The string is empty.")
        return

    print("Number of words:", len(words))

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)


def test_3() -> None:
    n = int(input("Enter n (n >= 2): "))
    if n < 2:
        print("n must be >= 2.")
        return

    numbers = []
    for i in range(n):
        num = int(input("Enter number " + str(i + 1) + ": "))
        numbers.append(num)

    result = []
    for i in range(n - 1):
        result.append(numbers[i] + numbers[i + 1])

    print("Sums of neighbors:", result)


def test_4() -> None:
    my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 20}

    asc = dict(sorted(my_dict.items()))
    print("Ascending by key:", asc)

    desc = dict(sorted(my_dict.items(), reverse=True))
    print("Descending by key:", desc)

    max_key = None
    max_val = None
    for key in my_dict:
        if max_val is None or my_dict[key] > max_val:
            max_val = my_dict[key]
            max_key = key

    print("Max value:", max_key, "=", max_val)


def test_5() -> None:
    products = {
        "cake": ["flour, sugar, eggs, cream", 250.0, 1500],
        "pastry": ["sponge, chocolate, cream", 180.0, 900],
        "muffin": ["flour, cocoa, raisins", 120.0, 700],
        "cookie": ["flour, butter, sugar", 90.0, 1200],
        "eclair": ["choux pastry, custard", 200.0, 600],
    }

    while True:
        print("\n===== CONFECTIONERY MENU =====")
        print("1. View description")
        print("2. View price")
        print("3. View quantity")
        print("4. All information")
        print("5. Purchase")
        print("6. Goodbye")

        choice = input("Choose a menu item: ")

        if choice == "1":
            for name in products:
                print(name, "-", products[name][0])

        elif choice == "2":
            for name in products:
                print(name, "-", products[name][1], "RUB per 100 g")

        elif choice == "3":
            for name in products:
                print(name, "-", products[name][2], "g")

        elif choice == "4":
            print("\n--- All information ---")
            for name in products:
                print(name + ":")
                print("  Ingredients:", products[name][0])
                print("  Price per 100 g:", products[name][1], "RUB")
                print("  Quantity:", products[name][2], "g")

        elif choice == "5":
            total = 0.0
            purchased = []

            print("\nEnter product name and quantity (in grams).")
            print("To exit purchase mode, type 'n' instead of a product name.")

            while True:
                name = input("Product name (or 'n' to exit): ").lower()
                if name == "n":
                    break

                if name not in products:
                    print("No such product. Try again.")
                    continue

                try:
                    amount = int(input("Quantity (g): "))
                except ValueError:
                    print("Invalid quantity.")
                    continue

                if amount <= 0:
                    print("Quantity must be positive.")
                    continue

                available = products[name][2]
                if amount > available:
                    print("Not enough product. Available:", available, "g.")
                    continue

                price_per_100 = products[name][1]
                cost = price_per_100 * amount / 100
                total += cost
                products[name][2] -= amount
                purchased.append((name, amount, cost))
                print("Added:", name, amount, "g for", round(cost, 2), "RUB.")

            if len(purchased) > 0:
                print("\n--- Receipt ---")
                for item in purchased:
                    print(item[0] + ":", item[1], "g -", round(item[2], 2), "RUB")
                print("Total to pay:", round(total, 2), "RUB")

                print("\n--- Remaining stock ---")
                for name in products:
                    print(name + ":", products[name][2], "g")
            else:
                print("No purchases made.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid menu item. Try again.")


def test_6() -> None:
    data = input("Enter integers separated by spaces: ")
    parts = data.split()

    numbers_list = []
    for x in parts:
        numbers_list.append(int(x))

    numbers = tuple(numbers_list)

    if len(numbers) == 0:
        print("The tuple is empty.")
        return

    sorted_numbers = tuple(sorted(numbers, reverse=True))

    print("Sorted tuple (descending):", sorted_numbers)
    print("First element:", sorted_numbers[0])
    print("Last element:", sorted_numbers[-1])