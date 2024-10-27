def is_int(s):
    """
    Проверка на то, что s - целое число
    """
    return True


def menu_sub1():
    print("menu_sub1 \n")


def menu_sub2():
    print("menu_sub2 \n")


def menu_main():
    """
    Циклическое. Выход из меню только через пункт 0
    """
    while True:
        print("menu_main \n 1) menu_sub1 \n 2) menu_sub2 \n 0) exit \n")
        ch = input()
        if is_int(ch):
            ch = int(ch)
        if ch == 1:
            menu_sub1()
        elif ch == 2:
            menu_sub2()
        elif ch == 0:
            break
        else:
            print('err')


if __name__ == "__main__":
    menu_main()
