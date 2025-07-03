carts = []  # List to store each cart's items

while True:
    user_input = input("> Enter number of shopping item in shopping cart {} or 'q' to exit : ".format(len(carts) + 1))
    
    if user_input.lower() == 'q':
        break

    try:
        num_items = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue

    current_cart = []  # Create a new list for each cart

    for i in range(1, num_items + 1):
        while True:
            try:
                price = float(input(f"> Enter price for item {i} : "))
                current_cart.append(price)
                break
            except ValueError:
                print("Invalid price. Please enter a valid number.")

    carts.append(current_cart)  # Append the new cart to carts list

# Compute totals and averages
total_price = sum([sum(cart) for cart in carts])
total_items = sum([len(cart) for cart in carts])
total_carts = len(carts)

average_item_price = total_price / total_items if total_items > 0 else 0
average_cart_price = total_price / total_carts if total_carts > 0 else 0

# Display results
print(f"\n> There are total of {total_carts} carts with total selling price {int(total_price)} "
      f"and average selling price of each item is {int(average_item_price)} "
      f"and average selling price of each cart is {int(average_cart_price)}")

for idx, cart in enumerate(carts, start=1):
    cart_total = sum(cart)
    cart_avg = cart_total / len(cart) if len(cart) > 0 else 0
    item_list = ', '.join(str(int(price)) for price in cart)
    print(f"Cart {idx} with items : {item_list} (Avg price = {int(cart_avg)})")