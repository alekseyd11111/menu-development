from menu_template import start_menu


def menu_f1():
    print('f1(x)')
    input("pause", )


def menu_f2():
    print('f2(x)')


def menu_g1():
    print('g1(x)')
    input("pause", )


def menu_g2():
    print('g2(x)')
    input("pause", )


def menu_sub1():
    """
    Однократное выполнение действия и возврат в главное меню.
    """
    # Ввод корректного ch
    caption_start = "menu_sub1 \n 1) f1(x) \n 2) f2(x) \n 0) return \n"
    caption_err = 'err'
    menu_template = {
        0: (lambda: True, True),
        1: (menu_f1, True),
        2: (menu_f2, True)}
        
    start_menu(caption_start, caption_err, menu_template)


def menu_sub2():
    """
    Циклическое. Возврат в главное меню только через пункт 0.
    """
    caption_start = "menu_sub2 \n 1) g1(x) \n 2) g2(x) \n 0) return \n"
    caption_err = 'err'   
    menu_template = {
        0: (lambda: True, True),
        1: (menu_g1, False),
        2: (menu_g2, False)}
    
    start_menu(caption_start, caption_err, menu_template)


def menu_main():
    """
    Циклическое. Выход из меню только через пункт 0
    """
    caption_start = "menu_main \n 1) menu_sub1 \n 2) menu_sub2 \n 0) exit \n"
    caption_err = 'err'
    menu_template = {
        0: (lambda: True, True),
        1: (menu_sub1, False),
        2: (menu_sub2, False)}  
    start_menu(caption_start, caption_err, menu_template)


if __name__ == "__main__":
    menu_main()
    exit(0)
