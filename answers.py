def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount=(discount_percent*0.01) * price
        final_price=price - discount
        print(f'The final price after applying the discount is: Ksh {final_price}')
    else:
        final_price= price
        print(f'No discount applied. The price remains: Ksh {price}')

# Prompt the user for input
try:
    price=float(input('Enter the original price: '))
    discount_percent=float(input('Enter the discount_percent: '))
    calculate_discount(price, discount_percent)
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")  