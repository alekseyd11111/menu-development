def is_int(s):
    """
    Проверка на то, что s - целое число
    """
    try:
        if type(s) is int:
            return True
        if s is None:
            return False
        if not s.isdecimal():
            return False
        int(s)
        return True
    except (Exception, ValueError, TypeError):
        return False


def entering_valid_value_integer(message_input: str, message_err: str, template: list):
    """
    Ввод допустимого целого числа
    :param message_input: Сообщение перед вводом
    :param message_err:   Сообщение при вводе символа, не из шаблона
    :param template:      Список допустимых значений
    :return: целое число
    """
    while True:
        ch = input(message_input, )
        if is_int(ch):
            ch = int(ch)
            if ch in template:
                return ch
        print(message_err)


def menu_sub1():
    """
    Однократное выполнение действия и возврат в главное меню
    """
    # Ввод корректного ch
    caption_start = "menu_sub1 \n 1) f1(x) \n 2) f2(x) \n 0) return \n"
    caption_err = 'err'
    template = [1, 2, 0]
    ch = entering_valid_value_integer(caption_start,
                                      caption_err,
                                      template)
    # Выбор действия
    match ch:
        case 1:
            print('f1(x)')
            input("pause", )
        case 2:
            print('f2(x)')
            input("pause", )
    # возврат в главное меню


def menu_sub2():
    """
    Циклическое. возврат в главное меню только через пункт 0
    """

    caption_start = "menu_sub2 \n 1) g1(x) \n 2) g2(x) \n 0) return \n"
    caption_err = 'err'
    template = [1, 2, 0]

    while True:
        # Ввод корректного ch
        ch = entering_valid_value_integer(caption_start,
                                          caption_err,
                                          template)
        # Выбор действия
        match ch:
            case 1:
                print('g1(x)')
                input("pause", )
            case 2:
                print('g2(x)')
                input("pause", )
            case 0:
                break
    # возврат в главное меню


def menu_main():
    """
    Циклическое. Выход из меню только через пункт 0
    """
    caption_start = "menu_main \n 1) menu_sub1 \n 2) menu_sub2 \n 0) exit \n"
    caption_err = 'err'
    template = [1, 2, 0]
    while True:
        # Ввод корректного ch
        ch = entering_valid_value_integer(caption_start,
                                          caption_err,
                                          template)
        # Выбор действия
        match ch:
            case 1:
                menu_sub1()
            case 2:
                menu_sub2()
            case 0:
                break
    # завершение программы


if __name__ == "__main__":
    menu_main()
    # exit(0)
