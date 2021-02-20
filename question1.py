cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
# Adds each letter as a separate item, must have square brackets as same type. append takes one argument
cheese += ['Oke']
print(cheese)
cheese.extend(['Oke', 'Brie'])
print(cheese)