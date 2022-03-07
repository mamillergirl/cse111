
from datetime import datetime


current_date_and_time = datetime.now()




    
import math

more_tire = "yes"

while more_tire == "yes":
    w = int(input('Enter the width of the tire in mm (ex 205): '))
    a = int(input('Enter the aspect ratio of the tire (ex 60): '))
    d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    pi = math.pi
    v = (pi * (w ** 2) * a * ( w * a + 2540 * d)) / 10000000000
    v = round(v , 2)
    print(f'The approximate volume is {v} liters')
    

    if d <= 15:
        size = "small"
        price = 110
    elif d <= 20:
        size = "medium"
        price = 175
    elif d >= 21:
        size = "large"
        price = 200
    total_price = price * 4
    print(f'The price per tire of a {size} tire is ${price}. ${total_price} in total.')
    
    with open('volumes.txt', 'at') as  volumes_text:
        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v}, ${price}, ${total_price}', file = volumes_text)
    
    buy_tire = input('Do you want to buy tires with these dimensions(yes/no)?  ').lower()
    if buy_tire == "yes":
        phone_number = input("Please enter your phone number:  ")
        with open('volumes.txt', 'at') as  volumes_text:
            print(phone_number, file = volumes_text)


   

    more_tire = input('Would you like to find the volume and price of another tire? ').lower()

    
