animal = input()

if animal == 'dog':
    animal = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal\
        == 'snake':
    animal = 'reptile'
else:
    animal = 'unknown'
print(animal)