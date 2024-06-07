spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

    return [key['name'] for key in spicy_foods]


def get_spiciest_foods(spicy_foods):
    pass

    return [ items for items in spicy_foods if items['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    pass

    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶'  * item['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    pass

    for item in spicy_foods:
        if item["heat_level"] > 5:
            print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶'  * item['heat_level']}")


def get_average_heat_level(spicy_foods):
    pass
    return sum([item['heat_level'] for item in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    pass

    result = [items for items in spicy_foods]
    result.append(spicy_food)
    return result

new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
