from pymongo import MongoClient
import random

# Підключення до бази даних
client = MongoClient("mongodb://localhost:27017/")
db = client["alchemy"]

# Визначення порядкового номеру для назви колекції ingredients_list
collection_count = len([name for name in db.list_collection_names(
) if name.startswith("ingredients_list_")]) + 1

# Отримання даних з колекцій
ingredients = db.ingredients.find()
properties = db.properties.find()

# Перетворення курсорів в списки
ingredients_list = list(ingredients)
temp_properties_list = list(properties)

# Прибираємо зайві атрибути властивостей
properties_list = [[item['_id'], item['multiplier']]
                   for item in temp_properties_list]


def get_random_property_id(properties_list):
    # Вибирає випадковий ID властивості з урахуванням multiplier
    weights = [property[1] for property in properties_list]
    return random.choices(properties_list, weights=weights)[0][0]


def assign_property_id(ingredients_list, properties_list):
    # Присвоює кожному інгредієнту 4 унікальних ID властивостей
    for ingredient in ingredients_list:
        ingredient['property_ids'] = set()
        while len(ingredient['property_ids']) < 4:
            property_id = get_random_property_id(properties_list)
            ingredient['property_ids'].add(property_id)


# Викликаємо функцію для наповнення інгредієнтів властивостями
assign_property_id(ingredients_list, properties_list)

# Змінюємо формат значення властивостей для експорта в БД
for ingredient in ingredients_list:
    ingredient['property_ids'] = list(ingredient['property_ids'])

# Отримуємо нову назву для колекції
new_collection_name = f"ingredients_list_{collection_count}"

# Створюємо колекцію інгредієнтів з властивостями
collection = db[new_collection_name]
collection.insert_many(ingredients_list)
print(f"New collection {new_collection_name} was added to {db.name}")
