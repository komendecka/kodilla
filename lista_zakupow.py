shopping_dict = {
    'piekarnia': ['bułki', 'chleb', 'pączek'],
    'warzywniak': ['marchew', 'cebula', 'rukola']}
items_amount = 0
for shop,items in shopping_dict.items() :
    item_capital_letter = [item.capitalize() for item in items]
    shopping_list = ', '.join(item_capital_letter)
    shop_capital_letter = shop.capitalize()
    print(f"Idę do {shop_capital_letter} i kupuję tam {shopping_list}")
    items_amount += len(items)

print(f"W sumie kupuję {items_amount} produktów.")