veggies_price_per_kilo = float(input())
fruits_price_per_kilo = float(input())
total_kilos_veggie = int(input())
total_kilos_fruits = int(input())
total_price = veggies_price_per_kilo*total_kilos_veggie+\
              fruits_price_per_kilo*total_kilos_fruits
price_in_euro = total_price/1.94
print(f'{price_in_euro:.2f}')