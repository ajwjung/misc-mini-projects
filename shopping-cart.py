# Toy series
series = {
    "DUCKOO TROPICAL SERIES (D)": 10.99,
    "F.UN x REPOLAR FRUIT SERIES (R)": 13.99,
    "YUKI TRANSPARENT SERIES (Y)": 11.99
}

# Series codes
series_letters = {
    "D": "DUCKOO TROPICAL SERIES (D)",
    "R": "F.UN x REPOLAR FRUIT SERIES (R)",
    "Y": "YUKI TRANSPARENT SERIES (Y)"
}

print("Welcome to POPMART!")
command = ''
cart = {}
while command != "exit":
    command = input("What would you like to do? ").lower()
    selection, qty = '', 0
    subtotal = 0
    if command == "help":
        print("""Enter one of the following commands:
- 'BROWSE' to look at the selection in stock
- 'ADD' to add an item to your cart
- 'CART' to see existing items in your cart
- 'CHECKOUT' to checkout the items in your cart
- 'EXIT' to quit """)
    elif command == "browse":
        for k, v in series.items():
            print(f"\t{k}: ${v}")
    elif command == "add":
        print("What would you like to add?")
        selection = input("Please enter the corresponding series letter, D/R/Y: ").upper()
        item = series_letters.get(selection)
        qty = int(input("Please enter the quantity: "))
        cart[item] = qty
        print(f"{item} x{qty} has been added to your cart.")

        subtotal = qty * series.get(item)
    elif command == "cart":
        if cart:
            for k, v in cart.items():
                print(f"{k} x{v}\nTotal = ${subtotal}")
        else:
            print("Your cart is empty.")
    elif command == "checkout":
        print(f"Your total is {subtotal}")
        pay = input("Please select a method of payment (cash/card): ").lower()
        if pay == "cash" or pay == "card":
            print("Thank you for your payment, have a nice day! :)")
            break
        else:
            print("Please enter a valid form of payment.")
            continue
    elif command == "exit":
        break
