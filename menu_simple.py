from MenuTemplate import MenuTemplate


def menu_f1():
    print('f1(x)')
    input("pause")


def menu_f2():
    print('f2(x)')
    input("pause")


def menu_g1():
    print('g1(x)')


def menu_g2():
    print('g2(x)')


def menu_sub1():
    """
    Однократное выполнение действия и возврат в главное меню.
    """
    menu = MenuTemplate("menu_sub1")
    menu.add_item("1", "f1(x)", menu_f1, True)
    menu.add_item("2", "f2(x)", menu_f2, True)
    menu.add_item("0", "exit", is_exit=True)
    menu.start()


def menu_sub2():
    """
    Циклическое. Возврат в главное меню только через пункт 0.
    """
    menu = MenuTemplate("menu_sub2")
    menu.add_item("1", "g1(x)", menu_g1)
    menu.add_item("2", "g2(x)", menu_g2)
    menu.add_item("0", "exit", is_exit=True)
    menu.start()


def menu_main():
    """
    Циклическое. Выход из меню только через пункт 0
    """
    menu = MenuTemplate("menu_main")
    menu.add_item("1", "menu_sub1", menu_sub1)
    menu.add_item("2", "menu_sub2", menu_sub2)
    menu.add_item("0", "exit", is_exit=True)
    menu.start()


if __name__ == "__main__":
    menu_main()
    exit(0)
