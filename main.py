file_len = []
countt = 0

def file_print(file, f):
    a = file.name.replace('.txt', '')
    print(file.name)
    print((len(f)))
    count = 1
    for i in f:
        print(f'Строка номер {count} файл номер {a}')
        count += 1
    count = 1

with open('1.txt', 'rt') as file:
    f = file.readlines()
    file_len.append(len(f))
with open('2.txt') as file2:
    f2 = file2.readlines()
    file_len.append(len(f2))
with open('3.txt') as file3:
    f3 = file3.readlines()
    file_len.append(len(f3))


while countt <= 2:
    if len(f) == min(file_len):
        file_print(file, f)
    if len(f2) == min(file_len):
        file_print(file2, f2)
    if len(f3) == min(file_len):
        file_print(file3, f3)
    file_len.remove(min(file_len))
    countt += 1
