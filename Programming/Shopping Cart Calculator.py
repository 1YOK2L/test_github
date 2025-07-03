price_list = []
cart = 0
h = 0

while (x := input(f"> Enter number of shopping item in shopping cart {h+1} or \'q\' to exit : ")) != 'q':
    if x.isnumeric:
        x = int(x)
        if x == 0:
            print("> The cart is empty.")
    for i in range(1, x+1):
        item_price = int(input(f"> Enter price for item {i} : "))
        price_list.append(item_price)
    cart += 1
    h += 1
print()
print(f"> There are total of {cart} carts with total selling price {sum(price_list)} and average selling price of each item is {int(sum(price_list)/len(price_list))} and average selling price of each cart is {int(sum(price_list)/cart)}")