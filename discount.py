# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(price, discount_percent)

    # Print result
    if discount_percent >= 20:
        print(f"Discount applied. Final price: {final_price}")
    else:
        print(f"No discount applied. Final price: {final_price}")
except ValueError:
    print("Please enter valid numbers for price and discount.")
