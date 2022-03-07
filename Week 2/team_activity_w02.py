from datetime import datetime
datetime.now(tz=None)

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

subtotal = float(input('Enter subtotal: '))

discount = subtotal * .10 

if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        subtotal = subtotal - discount
        print(f'Discount amount: {discount:.2f} ')
    else:
        amount_needed = 50 - subtotal
        print(f'You need ${amount_needed} to get the discount')

sales_tax = subtotal * .06
price = subtotal + sales_tax 

print(f'Sales tax amount: {sales_tax:.2f}')
print(f'Total: {price:.2f}' )
    