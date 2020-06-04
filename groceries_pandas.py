# groceries.py

# csv-mgmt/read_teams.py

import operator

import pandas

csv_filepath = "products.csv"

df = pandas.read_csv(csv_filepath)

products = df.to_dict("records")

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"(${my_price:,.2f})"

sorted_list = sorted(products, key=lambda x: x["name"])
department_list = []

print("---------------")
print("THERE ARE", len(sorted_list), "PRODUCTS")
print("---------------")

for x in sorted_list:
    if x["department"] not in department_list:
        department_list.append(x["department"])
        print("+", x["name"],to_usd(float(x["price"])))


print("---------------")
print("THERE ARE", len(department_list), "DEPARTMENTS")
print("---------------")

department_list = sorted(department_list)  

for dept_name in department_list:
    matching_products = len([x for x in products if x["department"] == dept_name])
    if matching_products > 1:
        print(f"+ {dept_name.title()} ({matching_products} products)")
    else:
        print(f"+ {dept_name.title()} ({matching_products} product)")

# print([x["department"] for x in products if x["department"] == "snacks"][0])

# TODO: write some Python code here to produce the desired output