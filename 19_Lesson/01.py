def market_system():
    print("Welcome! We are glad to have at our store!")
    products = {
        "milk" : {"category": "drinks", "price": 4},
        "bread" : {"category": "bakery", "price": 2},
        "apple" : {"category": "fruits", "price": 3},
        "egg" : {"category": "dairy and proteins", "price": 5},
        "cheese" : {"category": "dairy", "price": 6},
        "sausage" : {"category": "meat", "price": 8},
    }
    selected = []
    while True:
        print("\nproducts and their price: ")
        for i, j in products.items():
            print(f"- {i} ({j['category']}): {j['price']} TMT")
        product = input("Enter the product or type 'done' to finish: ")
        if product == 'done':
            break
        elif product not in products:
            print("Sorry, that product is not available. Please choose another.")
            continue
        count = input("Enter the quantity: ")
        selected.append((product, int(count)))            
    total = 0
    for i, count in selected:
        price = products[i]["price"]
        total += price * count
        print(f"{i} X {count}: {price * count} TMT")
    print(f"\nYour total payment: {total} TMT")
    print("Thank you for shopping with us!")

market_system()