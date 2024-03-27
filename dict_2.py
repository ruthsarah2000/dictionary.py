'''
2. Advanced Data Handling with Python
Task 1: Hotel Room Booking Tracker
Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

Problem Statement:
Develop a program that:

Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
Implement functions to:
Book a room (mark as booked and assign to a customer).
Check-out a customer (mark room as available and remove customer name).
Display the status of all rooms.
Start with this initial hotel room structure:
'''

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

hotel_rooms['103'] = {"status":"available", "customer": ""}
hotel_rooms['104'] = {"status":"available", "customer": ""}
hotel_rooms['105'] = {"status":"booked", "customer": "Jane Blye"}
hotel_rooms['106'] = {"status":"available", "customer": ""}
hotel_rooms['107'] = {"status":"booked", "customer": "Sandy Beaches"}
hotel_rooms['108'] = {"status":"available", "customer": ""}
hotel_rooms['109'] = {"status":"booked", "customer": "Palm Streets"}
hotel_rooms['110'] = {"status":"booked", "customer": "Vernon Stitch"}

hotel_rooms['107']['status'] = "available"
hotel_rooms['107']['customer'] = ""
print(hotel_rooms)

'''
Task 2: E-commerce Product Search Feature
Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

Problem Statement:
Create a system that:

Holds a dictionary of products where each product has attributes like name, category, and price.
Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
Handle cases where no matches are found.
Example product dictionary:
'''

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

products['3'] = {"name": "Pants", "category": "Clothing", "price": 30}
products['4'] = {"name": "Bread", "category": "Food", "price": 5}
products['5'] = {"name": "Bike", "category": "Toy", "price": 100}
products['6'] = {"name": "Sandals", "category": "Foot wear", "price": 10}
products['7'] = {"name": "Shoes", "category": "Foot wear", "price": 25}
products['8'] = {"name": "Leash", "category": "Pet supplies", "price": 8}
products['9'] = {"name": "Dress", "category": "Clothing", "price": 40}
products['10'] = {"name": "Snickers", "category": "Snack", "price": 1}

def search_product_by_name(products, search_term):
    matching_products = []
    for product_id, product_info in products.items():
        if search_term.lower() in product_info['name'].lower():
            matching_products.append((product_id, product_info))
    return matching_products

search_term = input("Enter the product name to search: ")
matching_products = search_product_by_name(products, search_term)

if matching_products:
    print("Matching products found:")
    for product_id, product_info in matching_products:
        print(f"Product ID: {product_id}, Name: {product_info['name']}, Category: {product_info['category']}, Price: ${product_info['price']}")
else:
    print("No matching products found.")
