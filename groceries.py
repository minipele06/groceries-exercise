# groceries.py

#from pprint import pprint

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"(${my_price:,.2f})" #> $12,000.71

def depo_convert(num):
    if num > 1:
        return f"({num} products)"
    else:
        return f"({num} product)"

def babies(obj):
    return obj["department"] == "babies"

def beverages(obj):
    return obj["department"] == "beverages"

def dairy(obj):
    return obj["department"] == "dairy eggs"

def dry(obj):
    return obj["department"] == "dry goods pasta"

def frozen(obj):
    return obj["department"] == "frozen"

def household(obj):
    return obj["department"] == "household"

def meat(obj):
    return obj["department"] == "meat seafood"

def pantry(obj):
    return obj["department"] == "pantry"

def personal(obj):
    return obj["department"] == "personal care"

def snacks(obj):
    return obj["department"] == "snacks"

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

sorted_list = sorted(products, key=lambda x: x["name"])
department_list = []

print("---------------")
print("THERE ARE", len(sorted_list), "PRODUCTS")
print("---------------")

for x in sorted_list:
    department_list.append(x["department"])
    print("+", x["name"],to_usd(x["price"]))
# pprint(products)

babies_count = len(list(filter(babies,products)))
beverages_count = len(list(filter(beverages,products)))
dairy_count = len(list(filter(dairy,products)))
dry_count = len(list(filter(dry,products)))
frozen_count = len(list(filter(frozen,products)))
household_count = len(list(filter(household,products)))
meat_count = len(list(filter(meat,products)))
pantry_count = len(list(filter(pantry,products)))
personal_count = len(list(filter(personal,products)))
snacks_count = len(list(filter(snacks,products)))
department_list = list(set(department_list))

print("---------------")
print("THERE ARE", len(department_list), "DEPARTMENTS")
print("---------------")
print("+ Babies",depo_convert(babies_count))
print("+ Beverages",depo_convert(beverages_count))
print("+ Dairy Eggs",depo_convert(dairy_count))
print("+ Dry Goods Pasta",depo_convert(dry_count))
print("+ Frozen",depo_convert(frozen_count))
print("+ Household",depo_convert(household_count))
print("+ Meat Seafood",depo_convert(meat_count))
print("+ Pantry",depo_convert(pantry_count))
print("+ Personal Care",depo_convert(personal_count))
print("+ Snacks",depo_convert(snacks_count))
# TODO: write some Python code here to produce the desired output