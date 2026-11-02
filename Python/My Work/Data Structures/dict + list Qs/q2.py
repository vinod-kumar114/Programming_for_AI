

# ================= Pattern 2: List of Nested Dictionaries =======================
# ================= (Database Rows / E-Commerce Shopping Cart Processing) ========



# 1. DATA STRUCTURE
cart = [
    {
        "item_id": 101,
        "name": "Laptop",
        "details": {"price": 1200, "qty": 1, "category": "Electronics"}
    },
    {
        "item_id": 102,
        "name": "Mouse",
        "details": {"price": 25, "qty": 3, "category": "Electronics"}
    },
    {
        "item_id": 103,
        "name": "Notebook",
        "details": {"price": 5, "qty": 10, "category": "Stationery"}
    }
]


# 2. ACTION: Specific Category ka Total Bill calculate karna + Discount apply karna
target_category = "Electronics"
grand_total = 0

for item in cart:
    # Nested Dict ke andar check karna
    if item["details"]["category"] == target_category:
        item_total = item["details"]["price"] * item["details"]["qty"]
        # Apply 10% discount on electronics
        item_total *= 0.90
        grand_total += item_total
        print(f"Item: {item['name']} | Discounted Total: ${item_total:.2f}")


print(f"\nFinal Total for {target_category}: ${grand_total:.2f}")