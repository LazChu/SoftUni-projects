number_chicken_menus=int(input())
numbers_fish_menus=int(input())
numbers_veggie_menus=int(input())
chicken_menu=10.35
fish_menu=12.40
veggie_menu=8.15
delivery=2.50
food_price=(number_chicken_menus*chicken_menu)+(numbers_fish_menus*fish_menu)\
    +(numbers_veggie_menus*veggie_menu)
desert=food_price*0.20
price=food_price+desert+delivery
print(price)