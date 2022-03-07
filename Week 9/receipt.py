import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Print the current day of the week and the current time.


def main():
    PRODUCT_ID_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    QUANTITY_INDEX = 1
    PRICE_INDEX = 2

    print('Inkom Emporium: \n ')
    products_dict = read_dict('products.csv', PRODUCT_ID_INDEX)
    process_requests(products_dict, PRODUCT_ID_INDEX, PRODUCT_NAME_INDEX, PRICE_INDEX, QUANTITY_INDEX)
    print('\nThank you for shopping at the Inkom Emporium')
    print(f"{current_date_and_time:%A %I:%M %p}")
            
    
   
def process_requests(products_dict, PRODUCT_ID_INDEX, PRODUCT_NAME_INDEX, PRICE_INDEX, QUANTITY_INDEX):
    total_quantity = 0
    subtotal = 0
    with open('request.csv', 'rt') as request_file:
        reader = csv.reader(request_file)
        next(reader)
        for row_list in reader:
            id = row_list[PRODUCT_ID_INDEX] 
            if id in products_dict:
                product_attribute_list = products_dict[id]
                name = product_attribute_list[PRODUCT_NAME_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])
                price = float(product_attribute_list[PRICE_INDEX])
                total_quantity += quantity
                quantity_price = price * quantity
                subtotal += quantity_price
                print(f'{name} : {quantity} @ {price}')


    sales_tax = subtotal * .06
    total = sales_tax + subtotal
    print(f'\nNumber of items: {total_quantity} \nSubtotal: {subtotal:.2f} \nSales Tax: {sales_tax:.2f} \nTotal: {total:.2f}')                
  
            


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as product_file:
        reader = csv.reader(product_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

        
        

    return dictionary
    

if __name__ == "__main__":
    main()
