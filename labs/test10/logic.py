def calculate(food, drink, dessert, tipamt):
    subtotal = food + drink + dessert
    tax = subtotal * 0.10
    tip = (subtotal + tax) * (tipamt / 100)
    total = subtotal + tax + tip
    return {
            "Food": food,
            "Drink": drink,
            "Dessert": dessert,
            "Tax": tax,
            "Tip": tip,
            "TOTAL": total
            }
