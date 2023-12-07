#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Используя замыкания функций, объявите внутреннюю функцию, которая принимает
# в качестве аргумента список целых чисел и удаляет из него все четные или
# нечетные значения в зависимости от значения параметра type . Если type
# равен «even», то удаляются четные значения, иначе – нечетные. По умолчанию
# type должно принимать значение «even». Вызовите внутреннюю функцию замыкания
# и отобразите на экране результат ее работы.

def del_items(type_param='even'):
    """
    Выбирается тип элементов для удаления.

    Можно выбрать 'even' - удалятся четные;
    иначе не четные. По умолчанию стоит 'even'.
    """
    def delete(list_items):
        """
        Функция удалет некоторые элементы массива в зависимости от type_param.

        Type_param задается во внешней функции.
        """
        match type_param:
            case 'even':
                return list(filter(lambda x: x % 2 != 0, list_items))
            case _:
                return list(filter(lambda x: x % 2 == 0, list_items))
    return delete


if __name__ == "__main__":
    start_items = [0, 1, 2, 3, 4, 5, 23, 21, 14, 72]
    print(f"\n{start_items=}\n")

    del_even = del_items()
    print(f"{del_even(start_items)=}\n")

    del_not_even = del_items('not even')
    print(f"{del_not_even(start_items)=}\n")
