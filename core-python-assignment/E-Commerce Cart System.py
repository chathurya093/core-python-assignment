def calculate_total(cart_items):
    if not cart_items:
        print("Cart is empty.")
        return 0, 0

    original_total = sum(cart_items.values())

    if len(cart_items) > 5:
        discount = original_total * 0.10
        final_total = original_total - discount
        return original_total, final_total
    else:
        return original_total, original_total

def main():
    cart_items = {}
    print("Enter your cart items one by one.")
    print("When you are done entering items, type 'done' for the item name.")

    while True:
        name = input("Item name (or 'done'): ")
        if name.lower() == 'done':
            break
        price_str = input(f"Price for \"{name}\": ")
        try:
            price = float(price_str)
            cart_items[name] = price
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue

    original, final = calculate_total(cart_items)

    if len(cart_items) > 5:
        print(f"Total: {int(original)}")
        print(f"After 10% discount: {int(final)}")
    else:
        print(f"Total Price: {int(final)}")

if __name__ == "__main__":
    main()
