animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations
animals.append('Raccoon')
animals.extend(wild_animals)
animals.pop(2)
animals.pop()
animals.insert(2, 'Moose')

print(animals)
