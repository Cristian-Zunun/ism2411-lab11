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

print("--- Exercise 5 ----") 
tier_discounts = { 
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.10, 
    "platinum": 0.15
}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate) 
print(f"Tier: {customer['tier']}") 
print(f"Discount: {discount_rate * 100:.0f}%") 
print(f"Final price: ${final_price:.2f}") 

print("--- Exercise 6 ---") 
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200}, 
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750}, 
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]
for record in customers: 
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate 
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")
