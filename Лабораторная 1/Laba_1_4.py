users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

set_mian = set(users)

dictionary_main = {
    "Общее количество":0,
    "Уникальные посещения":0
}

dictionary_main["Общее количество"] = len(users)
dictionary_main["Уникальные посещения"] = len(set_mian)

print(dictionary_main)