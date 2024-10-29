def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        for i, string in enumerate(strings):
            c = f.tell()
            f.write(string + '\n')
            b = i + 1, c
            a ={b: string}
            strings_positions.update(a)
            

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

