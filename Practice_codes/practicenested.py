fruits = ["apple","banana","pineapple","Orange"]

for index, name in enumerate(fruits):
    print(f'{index} {name}')
    
value=[(index, name) for index, name in enumerate(fruits)]
print(value)