import random
import json

NB_ITEMS: int = 10

names: list[str] = [
    random.choice(['John', 'Jane', 'Mary']) for _ in range(NB_ITEMS)
]

def generate_dicts():
    """
    Generates random dicts.
    """
    for name in names:
        yield {
            'name': name, 
            'surname': random.choice(['Doe', 'Smith', 'Jones']),
            'age': random.randint(18, 60)
        }

# print a generator
generator = generate_dicts()
print(*generator, sep="\n")
