# Задача 34 Найти количество гласных в каждой строке. Строки разделяются
# пробелами. Если количество гласных во всех строках одинаковое вывести
# Парам пам-пам, иначе Пам парам

def gls_in_line_cnt(line):
    gls = "аеиоуюя"
    gls_count = 0
    for letter in gls:
        gls_count += line.count(letter)

    return gls_count

def gls_in_text_check(text):
    line_list = text.split()
    ref_value = gls_in_line_cnt(line_list[0])
    gls_iterator = map(gls_in_line_cnt,line_list[1::])

    for value in gls_iterator:
        if value != ref_value:
            return False

    return True

test_poem = "пару-ра-рам рам-пам-папам па-ра-па-ди"

if gls_in_text_check(test_poem):
    print("Парам пам-пам")
else:
    print("Пам парам")




