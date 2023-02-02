bitcoin = int(input())
chinese_yoan = float(input())
commission = float(input())

# bitcoin = 1168 lv
# chinese_yoan = 0.15 $
# dollar = 1.76 lv
# euro = 1.95 lv
bitcoins = bitcoin * 1168
dollars = chinese_yoan * 0.15
leva = dollars * 1.76
total_leva = bitcoins + leva
euro = total_leva / 1.95
commission_taken = euro * commission / 100
total_money = euro - commission_taken
print(f'{total_money:.2f}')