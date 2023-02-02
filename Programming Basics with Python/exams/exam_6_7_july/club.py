amount_wanted = float(input())

cocktail = input()

income_amount = 0
while cocktail != 'Party!':
    number_of_cocktails = int(input())
    cocktail_len = len(cocktail)
    price = number_of_cocktails * cocktail_len
    if price % 2 != 0:
        price *= 0.75
    income_amount += price
    if amount_wanted <= income_amount:
        print("Target acquired.")
        break
    cocktail = input()
diff = abs(amount_wanted - income_amount)
if cocktail == 'Party!':
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {income_amount:.2f} leva.")