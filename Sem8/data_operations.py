def create_record(last_id):
    full_name = input("Введите полное имя (ФИО): ")
    phone     = input("Введите номер телефона: ")
    address   = input("Введите адрес: ")

    with open("phone_book.txt", 'a') as pb:
        pb.write(f'{last_id+1}\n{full_name}\n{phone}\n{address}\n\n')

    with open("id_list.txt", 'a') as id_file:
        id_file.write(f'{last_id+1}\n')

def search_record():
    srch_type = int(input("Введите тип поискового запроса (1 - ФИО, 2 - телефон, 3 - адрес): "))
    srch_txt  = input("Введите поисковый запрос: ")
    result_flag = False

    with open("phone_book.txt", 'r') as pb:
        cur_record = []

        while True:
            try:
                cur_record = list([next(pb) for x in range(5)])

                if srch_txt in cur_record[srch_type]:
                    result_flag = True
                    print('id = ', str(cur_record[0]).strip())
                    for i in range(1,4):
                        print(str(cur_record[i]).strip())
                    print()

                cur_record.clear()
            except:
                #бработка окончания файла
                if not result_flag:
                    print("Сответствия не найдены")
                break


def data_edit():
    user_id    = int(input("Введите id пользователя для редактирования (отображается при поисковом запросе): "))
    edit_field = (input("Введите через пробел номера полей для редактирования (1 - ФИО, 2 - телефон, 3 - адрес): ")).split()
    result_flag = False

    for element in edit_field:
        if int(element) < 1 or int(element) > 3:
            print("Некорректные поля для редактирования")
            return

    with open("phone_book.txt", 'r') as pb:
        records = pb.read().strip().split("\n\n")

    with open("phone_book.txt", 'w') as pb:
        for record in records:
            record_list = record.replace("\n",' ').split()
            if int(record_list[0]) == user_id:
                result_flag = True
                for field in edit_field:
                    print("Введите новое значение поля "+field)
                    record_list[int(field)] = input()

                record = ''
                for element in record_list:
                    record += element + "\n"
            record_list.clear()

            pb.write(record)
            pb.write("\n\n")

    if not result_flag:
        print("Запись с заданным id не найдена")


def data_rm():
    user_id    = int(input("Введите id пользователя для удаления (отображается при поисковом запросе): "))
    result_flag = False

    with open("phone_book.txt", 'r') as pb:
        records = pb.read().strip().split("\n\n")

    with open("phone_book.txt", 'w') as pb:

        for record in records:
            record_list = record.replace("\n",' ').split()
            if int(record_list[0]) != user_id:
                pb.write(record)
                pb.write("\n\n")
            else:
                result_flag = True
                with open("id_list.txt", 'r') as id_file:
                    ids = id_file.read().strip().split("\n")
                    ids.pop(ids.index(str(user_id)))

                with open("id_list.txt", 'w') as id_file:
                    for id in ids:
                        id_file.write(f'{id}\n')


    if not result_flag:
        print("Запись с заданным id не найдена")