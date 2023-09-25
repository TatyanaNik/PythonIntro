from data_operations import *
import sys
import os

def interface():
    op_type = int(input("Введите тип операции (1 - добавить запись, 2 - найти котакт, "
                        "3 - редактировать запись, 4 - удалить запись, 5 - выход): "))

    if op_type == 1:

        open("id_list.txt", 'a').close()

        with open("id_list.txt", 'r') as id_file:
            if os.stat('id_list.txt').st_size != 0:
                ids = id_file.read().strip().split("\n")
                last_id = int(ids[-1])
            else:
                last_id = -1

        create_record(last_id)

    elif op_type == 2:
        search_record()
    elif op_type == 3:
        data_edit()
    elif op_type == 4:
        data_rm()
    elif op_type == 5:
        sys.exit()
    else:
        print("неизвестный код операции")

