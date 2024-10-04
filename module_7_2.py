def custom_write(file_name, strings):
    # Словарь для хранения позиций строк
    strings_positions = {}

    # Открываем файл для записи с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as f:
        for index, string in enumerate(strings, start=1):  # enumerate генерирует кортежи,
            # состоящие из индекса элемента и самого этого элемента.
            # Получаем текущую позицию байта
            byte_position = f.tell()
            # Сохраняем позицию и строку в словаре
            strings_positions[(index, byte_position)] = string
            # Записываем строку в файл с переводом на новую строку
            f.write(string + '\n')

    return strings_positions






info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
