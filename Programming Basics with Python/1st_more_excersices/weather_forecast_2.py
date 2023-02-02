tempereture = float(input())

if 26 <= tempereture <= 35:
    print(f'Hot')
elif 20.1 <= tempereture <= 25.9:
    print(f'Warm')
elif 15 <= tempereture <= 20:
    print(f'Mild')
elif 12 <= tempereture <= 14.9:
    print(f'Cool')
elif 5<= tempereture <= 11.9:
    print(f'Cold')
else:
    print(f'unknown')