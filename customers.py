print("--- Exercise 1 ---") 
customer = { 
    "name": "Alice", 
    "email": "alice@example.com",
    "tier": "gold", 
    "ytd_spend": 12400, 
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142" 

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"] 

print(customer) 

print("--- Exercise 3 ---") 
print(customer.get("email", "no email on file")) # New
# Old version
# try:                                    
#     print(customer["email"]) 
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

print("--- Exercise 4 ---")
for key, value in customer.items(): 
    print(f"{key} : {value}") 
for item in customer: 
    print(item)  # Without using items, we are only going to get the keys