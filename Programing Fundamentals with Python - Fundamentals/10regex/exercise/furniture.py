# import re
#
# pattern = r">{2}([a-zA-Z]+)<{2}(\d+\.?\d*)!(\d+)"
#
# command = input()
# bought_items = []
# total_price = 0
# while command != 'Purchase':
#     matches = re.findall(pattern, command, )
#     if matches:
#         purchase = matches[0]
#         item = purchase[0]
#         bought_items.append(item)
#         price = float(purchase[1]) * int(purchase[2])
#         total_price += price
#         command = input()
#     else:
#         command = input()
#         continue
# print('Bought furniture:')
# for item in bought_items:
#     print(item)
# print(f"Total money spend: {total_price:.2f}")


import re

pattern = r">{2}([a-zA-Z]+)<{2}(\d+[\.?]*\d+)!(\d)"

command = input()
bought_items = []
total_price = 0
while command != 'Purchase':
    matches = re.findall(pattern, command, )
    if matches:
        purchase = matches[0]
        item = purchase[0]
        bought_items.append(item)
        price = float(purchase[1]) * int(purchase[2])
        total_price += price
        command = input()
    else:
        command = input()
        continue
print('Bought furniture:')
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")
